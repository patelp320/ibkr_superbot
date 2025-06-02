def run():
    print("✅ [OPTIONS] Running options wheel strategy")
    # TODO: Add live options logic here

if __name__ == "__main__":
    run()


def run_wheel_strategy():
    from bot.options_wheel import main
    main()

# ✅ Added by setup script to enable core.py entry
def main():
    print("Running options wheel main()")
    run_wheel()  # Replace 'run_wheel' with correct function name if needed
