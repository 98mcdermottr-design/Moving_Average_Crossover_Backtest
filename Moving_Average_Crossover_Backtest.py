
import yfinance as yf
# gets data from yahoo finance
import pandas as pd
# for tables, calculations, etc.
import numpy as np
# for numerical calculations (mean, std, etc.)
import matplotlib.pyplot as plt
# for plotting charts

def download_data(ticker, start, end):
#define function to be called later
    """Download historical data from Yahoo Finance""" #called docstring, like comment at beginning of function but doesn't affect code
# 3 quotations means you can write multi-line strings
    data = yf.download(ticker, start=start, end=end)
# downloads ticker data from yahoo finanace
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [col[0] for col in data.columns]
# ensures columns are just titled close, open, etc. Helps with references later on
    return data

def generate_signals(data, short_window=50, long_window=200):
    """Generate buy/sell signals using moving average crossover"""
    data["SMA50"] = data["Close"].rolling(short_window).mean()
#this adds a new column to the excel called SMA50 with the rolling 50 day mean closing prices
    data["SMA200"] = data["Close"].rolling(long_window).mean()
#the rolling function is used in conjunction with the mean function to take the mean of the last x values

    data["Signal"] = 0
# creates blank column essentially
    data.loc[data["SMA50"] > data["SMA200"], "Signal"] = 1   # long
    data.loc[data["SMA50"] < data["SMA200"], "Signal"] = -1  # short
# .loc makes it look at each row and compares the column values, then adds value to empty Signal column (comes from pandas package)
# essentially what the above does, if the 50 day moving average is above the 200 day moving average then you long the stock and vice versa to short the stock
    return data

def backtest_strategy(data):
    """Run backtest and calculate strategy performance"""
    data["Return"] = data["Close"].pct_change()
#looks at % change between current and previous value in column, then adds % change to Return column (comes from numpy package)
    data["Strategy"] = data["Signal"].shift(1) * data["Return"]
#since you don't know the strategy until the end of the day, whether to go long or short, as you don't have closing prices until end of trading_strategy_backtest
#the shift goes down 1 row in the column and then multiplies it by the return column
    data = data.dropna(subset=["SMA200"]).copy()
#this drops the observations until the average 200 kicks in
    cumulative_strategy = (1 + data["Strategy"]).cumprod()
    cumulative_benchmark = (1 + data["Return"]).cumprod()
#cumprod() multiplies each cell in column by each other to get the cumulative product
# we're making two columns, one with just a buy and hold strategy and one where you've used strategy

    sharpe_ratio = np.sqrt(252) * data["Strategy"].mean() / data["Strategy"].std()
# share ratio is just the annualised mean divided by the standard deviations.
# this is applied to the long/short strategy, not the buy+hold strategy
    return cumulative_strategy, cumulative_benchmark, sharpe_ratio, data

def plot_results(cumulative_strategy, cumulative_benchmark):
    """Plot strategy performance vs Buy & Hold benchmark"""
    plt.figure(figsize=(10, 6))
    # for chart size
    plt.plot(cumulative_benchmark, label="Buy & Hold")
    # plots buy and hold
    plt.plot(cumulative_strategy, label="Strategy")
    # plots long/short strategy
    plt.title("Trading Strategy vs Buy & Hold")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return (Growth of $1)")
    plt.legend()
    # to show labels
    plt.show()

# Parameters

ticker = input("Enter ticker (e.g. AAPL, MSFT, TSLA): ").upper().strip()
# just asking the user for one ticker, and then transforming the input to all upper case and without spaces
start = input("Enter start date (YYYY-MM-DD): ")
end = input("Enter end date (YYYY-MM-DD): ")


data = download_data(ticker, start, end)
# uses function defined above to get yahoo finance data

data = generate_signals(data)
# uses function above to do the long/short strategy
data.to_csv("historical data.csv")
# exports data into csv
cumulative_strategy, cumulative_benchmark, sharpe_ratio, data_valid = backtest_strategy(data)
#do this as function returns tuple, so your just directly assigning variables instead of having to reference tuple going forward
# Print results
print(f"\nTicker: {ticker}")
#the f ensures that the variable ticker is picked up and put in the sentence as a string
print(f"Sharpe Ratio: {sharpe_ratio:.2f}\n")
#the 2f turns the sharpe ratio into a floating point number with 2 decimals
print("Last few rows of data with signals:")
print(data.tail(10))
# just added to see all working well

# plot results
plot_results(cumulative_strategy, cumulative_benchmark)
