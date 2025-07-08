import pandas as pd
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bot.data import fetch_price_history

def test_fetch_price_history():
    df = fetch_price_history(["AAPL"], period="1d", interval="1d")
    assert isinstance(df, pd.DataFrame)
