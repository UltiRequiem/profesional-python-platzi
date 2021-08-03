from datetime import datetime as dt


def run():
    now = dt.utcnow()

    print(f"LATAM Format: {now.strftime('%d/%m/%Y')}")
    print(f"USA Format: {now.strftime('%m/%d/%Y')}")
    print(f"Default Format: {now}")


if __name__ == "__main__":
    run()
