import numpy as np
import pandas as pd

class QLearningTrader:
    def __init__(self, alpha: float = 0.1, gamma: float = 0.95, epsilon: float = 0.1):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def _get_state(self, row: pd.Series) -> str:
        direction = 'up' if row['Close'] >= row['Open'] else 'down'
        return direction

    def choose_action(self, state: str) -> str:
        if np.random.rand() < self.epsilon or state not in self.q_table:
            return np.random.choice(['buy', 'sell', 'hold'])
        return max(self.q_table[state], key=self.q_table[state].get)

    def update(self, state: str, action: str, reward: float, next_state: str):
        if state not in self.q_table:
            self.q_table[state] = {a: 0.0 for a in ['buy', 'sell', 'hold']}
        if next_state not in self.q_table:
            self.q_table[next_state] = {a: 0.0 for a in ['buy', 'sell', 'hold']}
        q_predict = self.q_table[state][action]
        q_target = reward + self.gamma * max(self.q_table[next_state].values())
        self.q_table[state][action] += self.alpha * (q_target - q_predict)

    def train(self, data: pd.DataFrame):
        for i in range(len(data) - 1):
            row = data.iloc[i]
            next_row = data.iloc[i + 1]
            state = self._get_state(row)
            next_state = self._get_state(next_row)
            action = self.choose_action(state)
            reward = next_row['Close'] - row['Close'] if action == 'buy' else row['Close'] - next_row['Close']
            self.update(state, action, reward, next_state)
