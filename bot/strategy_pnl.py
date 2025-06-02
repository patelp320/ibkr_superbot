from datetime import datetime

def generate_summary():
    # Dummy trades
    trades = [
        {"strategy": "PennyScanner", "pnl": 120},
        {"strategy": "OptionsWheel", "pnl": -30},
        {"strategy": "PennyScanner", "pnl": 80},
    ]

    summary = {}
    for t in trades:
        strat = t.get("strategy", "Unknown")
        summary.setdefault(strat, []).append(t["pnl"])

    lines = ["📊 Strategy Performance Summary (" + datetime.now().strftime("%Y-%m-%d") + ")"]
    for strat, results in summary.items():
        wins = sum(1 for x in results if x > 0)
        losses = sum(1 for x in results if x <= 0)
        net = sum(results)
        win_rate = wins / max(1, wins + losses) * 100
        lines.append(f"{strat}: Net=${net:.2f}, Win Rate={win_rate:.1f}%")

    print("\n".join(lines))