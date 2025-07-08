from ib_insync import MarketOrder, IB, Stock, Option
from typing import List

class IBExecutor:
    def __init__(self, host: str = '127.0.0.1', port: int = 7497, client_id: int = 1):
        self.ib = IB()
        self.ib.connect(host, port, client_id)

    def place_order(self, symbol: str, action: str, quantity: int, is_option: bool = False):
        contract = Option(symbol, '20250117', 0, 'C', 'SMART') if is_option else Stock(symbol, 'SMART', 'USD')
        order = MarketOrder(action, quantity)
        trade = self.ib.placeOrder(contract, order)
        return trade

    def disconnect(self):
        self.ib.disconnect()
