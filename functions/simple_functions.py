import datetime


def get_time():
    time_now = datetime.datetime.now().time()
    return f'It\'s {time_now.hour}:{time_now.minute}.'


