# IBKR Superbot

This repository contains a minimal example script that connects to the Interactive Brokers API using [`ib_insync`](https://github.com/erdewit/ib_insync). It retrieves account summary information and emails the result.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Fill in the `.env` file with your IB and SMTP credentials. An example `.env` is provided.

## Usage

Ensure your IB Gateway or Trader Workstation is running and listening on port `7497` (paper trading). Run the bot:

```bash
python ibkr_superbot.py
```

The script will fetch your account summary and send it via email.
