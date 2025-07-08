import yfinance as yf
import pandas as pd
from typing import List

def fetch_price_history(tickers: List[str], period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    """Fetch historical price data for tickers using yfinance."""
    data = []
    for ticker in tickers:
        try:
            df = yf.download(ticker, period=period, interval=interval, progress=False)
            if df.empty:
                continue
            df["Ticker"] = ticker
            data.append(df)
        except Exception as exc:
            print(f"Failed to download {ticker}: {exc}")
    if data:
        return pd.concat(data)
    return pd.DataFrame()
