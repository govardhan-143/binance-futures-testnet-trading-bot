# Binance Futures Testnet Trading Bot

This project is a Python-based CLI application that places Market and Limit orders on Binance Futures Testnet.

## Features

- Market Orders
- Limit Orders
- BUY and SELL support
- Input validation
- Logging
- Error handling

## Setup

1. Clone repository

2. Create virtual environment

3. Install dependencies

pip install -r requirements.txt

4. Create .env file

BINANCE_API_KEY= api_key
BINANCE_API_SECRET= secret_key

## Run

Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
