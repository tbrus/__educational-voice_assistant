import datetime


def get_time():
    time_now = datetime.datetime.now().time()
    return f'It\'s {time_now.hour}:{time_now.minute}.'


def get_today_date():
    date = datetime.datetime.now().strftime('%d of %B')
    date = str(date).lstrip('0')
    print(date)
    return f'Today is {date}.'


