import os
import difflib
from datetime import datetime

def check_and_patch():
    target = "penny_scanner.py"
    backup = f"{target}.bak"
    try:
        with open(target) as f:
            lines = f.readlines()
        if not lines:
            raise ValueError("Empty file")
    except Exception as e:
        print(f"[🛠] Self-Heal: Detected issue in {target}: {e}")
        if os.path.exists(backup):
            print("[🛠] Restoring from backup...")
            with open(backup) as b, open(target, "w") as f:
                f.write(b.read())
            print("[🛠] Recovery complete.")
        else:
            print("[🛠] No backup found. Cannot auto-fix.")
    else:
        print("[🛡️] Self-Heal: No issues detected.")