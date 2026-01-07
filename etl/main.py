from datetime import datetime, timezone

def main():
    print(f"Pipeline started at {datetime.now(timezone.utc)}")

if __name__ == "__main__":
    main()

