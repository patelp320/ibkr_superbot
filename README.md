# IBKR Superbot – Live Trading Blueprint (Tonight Ready)

This bot scans penny stocks, executes options trades, trains AI models, checks earnings calendars, monitors news, and places real trades via Interactive Brokers (IBKR). It's designed for high accuracy (targeting 90% win rate) and modular self-healing behavior.

---

## ✅ How to Run on Your MacBook (Paper or Live)

### 1. Unzip the downloaded file:
```
unzip ibkr_superbot_tonight_ready.zip
cd ibkr_superbot_clean_final
```

### 2. Set up a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install required packages:
```
pip install -r requirements.txt
pip install yfinance ib_insync schedule
```

### 4. Start your IB Gateway (or TWS):
- Use **Paper account**: port `7497`
- Use **Live account**: port `7496`
- Login, and leave it running

### 5. Run the bot:
```
python main_loop.py
```

You will see:
- Trades placed in IBKR
- Logs in `logs/bot.log`
- Trades saved in `logs/trade_journal.csv`

---

## 🔄 How to Move to Your NAS

### 1. Upload the ZIP to your NAS:
Use scp or drag/drop via file share:
```
scp ibkr_superbot_tonight_ready.zip your-nas-ip:/volume1/docker/
```

### 2. SSH into your NAS (if needed):
```
ssh your-nas-user@your-nas-ip
```

### 3. Unzip and set up:
```
unzip ibkr_superbot_tonight_ready.zip
cd ibkr_superbot_clean_final
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install yfinance ib_insync schedule
```

### 4. Start the bot:
```
python main_loop.py
```

---

## 📂 Files Overview

| File | Purpose |
|------|---------|
| `main_loop.py` | Master orchestrator running all modules |
| `ibkr_client.py` | IBKR connection, trade functions |
| `options_executor.py` | Places PUTs using IBKR |
| `penny_seller.py` | Sells penny stock positions |
| `predictor.py` | AI prediction model |
| `volume_surge.py`, `rsi_signal.py` | Blueprint scanners |
| `logs/` | Stores execution logs + CSV trade logs |

---

## ✅ Live Safety Features

- Earnings filter (blocks near-reporting stocks)
- Max capital per trade = 2% of NetLiquidation
- Trade retry timeout (cancel if not filled)
- Email alerts per cycle
- Fully modular: restart any part independently

---

For help: contact yourself 😎 or re-run `main_loop.py` with debug logs enabled.