from ib_insync import IB, Stock, Option, MarketOrder
import os

# Global connection object
ib = IB()

def connect_ibkr(paper=True):
    host = os.getenv('IB_HOST', '127.0.0.1')
    port = int(os.getenv('IB_PORT', 7497 if paper else 7496))
    client_id = int(os.getenv('IB_CLIENT_ID', 1))
    try:
        ib.connect(host, port, clientId=client_id)
        print(f"[IBKR] Connected to {'paper' if paper else 'live'} account.")
    except Exception as e:
        print(f"[IBKR] Connection failed: {e}")
        raise

def place_option_trade(symbol, strike, expiry, right='P', quantity=1):
    contract = Option(symbol, expiry, strike, right, 'SMART')
    order = MarketOrder('SELL', quantity)
    ib.qualifyContracts(contract)
    trade = ib.placeOrder(contract, order)
    print(f"[IBKR] Placed option trade: {quantity}x {symbol} {right}{strike} {expiry}")
    return trade

def buy_stock(symbol, quantity):
    stock = Stock(symbol, 'SMART', 'USD')
    order = MarketOrder('BUY', quantity)
    ib.qualifyContracts(stock)
    trade = ib.placeOrder(stock, order)
    print(f"[IBKR] Bought {quantity} shares of {symbol}")
    return trade

def sell_stock(symbol, quantity):
    stock = Stock(symbol, 'SMART', 'USD')
    order = MarketOrder('SELL', quantity)
    ib.qualifyContracts(stock)
    trade = ib.placeOrder(stock, order)
    print(f"[IBKR] Sold {quantity} shares of {symbol}")
    return trade

def disconnect_ibkr():
    ib.disconnect()

from datetime import datetime, timedelta
import yfinance as yf

def get_max_trade_size():
    account = ib.accountSummary()
    net_liq = float(account.loc['NetLiquidation', 'value'])
    return round(net_liq * 0.02, 2)  # Risk 2% of capital

def wait_for_fills(trade, timeout=10):
    ib.sleep(1)
    for _ in range(timeout):
        if trade.isDone():
            print("[✔] Trade Filled.")
            return True
        ib.sleep(1)
    print("[⚠️] Trade not filled in time. Cancelling.")
    ib.cancelOrder(trade.order)
    return False

def has_upcoming_earnings(symbol, days=3):
    try:
        cal = yf.Ticker(symbol).calendar
        if cal.empty:
            return False
        earnings_date = cal.iloc[0]['Earnings Date']
        return (earnings_date - datetime.now()).days <= days
    except Exception:
        return False