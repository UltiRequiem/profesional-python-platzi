from datetime import datetime as dt


def run(year, month, day):
    return f"Date: {year}-{month}-{day}"


if __name__ == "__main__":
    today = dt.today()
    print(run(today.year, today.month, today.day))
