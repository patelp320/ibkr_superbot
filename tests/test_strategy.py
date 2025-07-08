import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pandas as pd
from bot.strategy import QLearningTrader


def test_trader_learns():
    data = pd.DataFrame({
        'Open': [1, 2, 3],
        'Close': [2, 1, 4]
    })
    trader = QLearningTrader(alpha=0.5, gamma=0.9, epsilon=0.0)
    trader.train(data)
    assert trader.q_table
