import time
import yfinance as yf


def scan(tickers):
    results = {}
    for ticker in tickers:
        try:
            t = yf.Ticker(ticker)
            opts = t.options
            results[ticker] = opts
            print(f"{ticker}: {len(opts)} option expiration dates found.")
        except Exception as e:
            print(f"Error fetching {ticker}: {e}")
    return results


if __name__ == "__main__":
    tickers = ["AAPL", "GOOGL", "TSLA"]
    while True:
        print(f"Scanning tickers {tickers}")
        scan(tickers)
        time.sleep(60)

