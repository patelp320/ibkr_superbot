# IBKR Superbot

This repository contains a minimal example of a self-learning trading bot. It uses the `yfinance` package to download historical market data and a simple Q-learning algorithm for generating buy/sell/hold signals.

## Features
- Fetches historical prices for multiple tickers
- Basic Q-learning strategy that learns from price movements
- Skeleton code to connect to Interactive Brokers using `ib_insync` (see `bot/execution.py`)

## Running
```
python -m bot.main TICKER1 TICKER2
```
This will download recent price data and train the Q-learning trader. The resulting Q-table is printed for demonstration.

## Disclaimer
This code is for educational purposes only and should not be used for live trading without significant improvements and thorough testing. Penny stocks and options are highly risky and require careful analysis and compliance with regulations.
