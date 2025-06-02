import time
from datetime import datetime

from bot.predictor import main as run_predictor
from bot.penny_scanner import main as run_penny_scanner
from bot.options_wheel import main as run_options_wheel
from strategy_pnl import generate_summary
from profit_reporter import report_profits
from bot.options_executor import main as execute_options
from bot.news_scraper import main as scan_news
from bot.emailer import send_email
from self_learn import train_models
from bot.scheduler import run_scheduler
from self_heal import check_and_patch
from watchdog import monitor_processes

# Newly added blueprint modules
from volume_surge import detect_volume_surges
from rsi_signal import scan_rsi
from insider_activity_tracker import check_insider_trades
from gap_detector import detect_gaps
from earnings_calendar import upcoming_earnings
from anomaly_detector import detect_anomalies
from hype_tracker import get_social_hype

def log(msg):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{timestamp} {msg}")
    with open("logs/bot.log", "a") as f:
        f.write(f"{timestamp} {msg}\n")

def safe_run(name, fn):
    try:
        log(f"🚀 START {name}")
        fn()
        log(f"✅ DONE {name}")
    except Exception as e:
        log(f"❌ ERROR in {name}: {e}")

if __name__ == "__main__":
    for cycle in range(8):
        log(f"📊 SUPERBOT BLUEPRINT CYCLE {cycle + 1}")
        safe_run("PREDICTOR", run_predictor)
        safe_run("PENNY_SCANNER", run_penny_scanner)
        safe_run("OPTIONS_WHEEL", run_options_wheel)
        safe_run("STRATEGY_PNL", generate_summary)
        safe_run("PROFIT_REPORT", report_profits)
        safe_run("MODEL_TRAINING", train_models)
        safe_run("SCHEDULER", run_scheduler)
        safe_run("SELF_HEAL", check_and_patch)
        safe_run("WATCHDOG", monitor_processes)

        # Run newly added blueprint upgrades
        safe_run("VOLUME_SURGE", detect_volume_surges)
        safe_run("RSI_SIGNAL", scan_rsi)
        safe_run("INSIDER_ACTIVITY", check_insider_trades)
        safe_run("GAP_DETECTOR", detect_gaps)
        safe_run("EARNINGS_CALENDAR", upcoming_earnings)
        safe_run("ANOMALY_DETECTOR", detect_anomalies)
        safe_run("HYPE_TRACKER", get_social_hype)
        safe_run("OPTIONS_EXECUTOR", execute_options)
        safe_run("NEWS_SCRAPER", scan_news)
        safe_run("EMAILER", lambda: send_email(subject='Cycle Complete', body='Cycle {} completed.'.format(cycle + 1)))

        time.sleep(1)