# Moving Average Crossover Backtest

This project implements a simple **moving average crossover trading strategy** using Python.  
It downloads stock data from yahoo finance with `yfinance`, generates buy/sell signals from two moving averages (a 50 day moving average and a 200 day moving average), and compares the strategy’s performance to a buy-and-hold benchmark.

--

## 🧩 Features
- Downloads historical stock data via Yahoo Finance
- Computes 50-day and 200-day simple moving averages
- Generates trading signals (long/short)
- Backtests performance with Sharpe Ratio
- Plots cumulative returns

--

## 📈 Outcome
- Shows a chart comparing the two strategies
- If moving average crossover strategy outperforms buy and hold strategy, then consider implementing the strategy for that stock
- Note though, that less traded stocks often have higher trading fees, particulary when it comes to shorting stocks, so consider this before implementing the strategy as this model does not incorporate trading fees

--

## 📑Sources
- CFA curriculum - Level 1

--

## 🚀 How to Run
```bash
pip install yfinance pandas numpy matplotlib
python Moving_Average_Crossover_Backtest.py
