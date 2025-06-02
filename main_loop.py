print("🚀 Superbot Started Running")

import time
print("🟢 Bot is alive at", time.strftime("%Y-%m-%d %H:%M:%S"))

from bot.predictor import main as run_predictor
from bot.penny_scanner import main as run_penny_scanner
from bot.options_wheel import main as run_options_wheel
from bot.strategy_pnl import generate_summary
from bot.profit_reporter import report_profits
from bot.self_learn import train_models
from bot.scheduler import run_scheduler
from bot.self_heal import check_and_patch
from bot.watchdog import monitor_processes
from bot.emailer import send_email
from bot.news_scraper import main as scan_news
from bot.options_executor import main as execute_options

def safe_run(name, fn):
    try:
        print(f"[▶️] Running: {name}")
        fn()
        print(f"✅ Finished: {name}")
    except Exception as e:
        print(f"❌ Failed: {name} → {e}")

if __name__ == "__main__":
    safe_run("PREDICTOR", run_predictor)
    safe_run("PENNY_SCANNER", run_penny_scanner)
    safe_run("OPTIONS_WHEEL", run_options_wheel)
    safe_run("STRATEGY_PNL", generate_summary)
    safe_run("PROFIT_REPORT", report_profits)
    safe_run("MODEL_TRAINING", train_models)
    safe_run("SCHEDULER", run_scheduler)
    safe_run("SELF_HEAL", check_and_patch)
    safe_run("WATCHDOG", monitor_processes)
    safe_run("EMAILER", lambda: send_email("Cycle Complete", "Your bot finished one full run."))
    safe_run("NEWS_SCRAPER", scan_news)
    safe_run("OPTIONS_EXECUTOR", execute_options)
