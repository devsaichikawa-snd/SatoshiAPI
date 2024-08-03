import datetime


def get_sundays(year):
    """年間の日曜日の日付一覧を取得する"""

    # その年の1月1日を取得
    date = datetime.date(year, 1, 1)
    # 最初の日曜日を見つける
    while date.weekday() != 6:  # 6は日曜日
        date += datetime.timedelta(days=1)

    # 最初の日曜日から毎週の日曜日をリストに追加
    sundays = []
    while date.year == year:
        sundays.append(date)
        date += datetime.timedelta(days=7)

    return sundays


if __name__ == "__main__":
    sundays = get_sundays(2024)
    for sunday in sundays:
        print(sunday)
