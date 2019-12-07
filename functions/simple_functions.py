import datetime
import locale


def get_time():
    time_now = datetime.datetime.now().time()
    return f'Jest godzina {time_now.hour}:{time_now.minute}.'


def get_today_date():
    locale.setlocale(locale.LC_TIME, "pl_PL.utf8")
    date = datetime.datetime.now().strftime('%d %B')
    date = str(date).lstrip('0')
    print(date)
    return f'Dzisiaj jest {date}.'


