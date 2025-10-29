# Moving Average Crossover Backtest

This project implements a simple **moving average crossover trading strategy** using Python.  
It downloads stock data with `yfinance`, generates buy/sell signals from two moving averages,  
and compares the strategy’s performance to a buy-and-hold benchmark.

## 📈 Features
- Downloads historical stock data via Yahoo Finance
- Computes 50-day and 200-day simple moving averages
- Generates trading signals (long/short)
- Backtests performance with Sharpe Ratio
- Plots cumulative returns

## 🚀 How to Run
```bash
pip install yfinance pandas numpy matplotlib
python Moving_Average_Crossover_Backtest.py
