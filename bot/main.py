import argparse
from .data import fetch_price_history
from .strategy import QLearningTrader
#from .execution import IBExecutor


def run(tickers):
    data = fetch_price_history(tickers, period="1mo", interval="1d")
    trader = QLearningTrader()
    trader.train(data)
    # For demonstration we just print the Q-table
    print(trader.q_table)


def main():
    parser = argparse.ArgumentParser(description="Simple self-learning trading bot")
    parser.add_argument('tickers', nargs='+', help='Tickers to trade')
    args = parser.parse_args()
    run(args.tickers)


if __name__ == '__main__':
    main()
