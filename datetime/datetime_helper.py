"""
%Y      Year with century, as in '2014'
%y      Year without century, '00' to '99' (1970 to 2069)
%m      Month as a decimal number, '01' to '12'
%d      Day of the month, '01' to '31'

%H      Hour (24-hour clock), '00' to '23'
%M      Minute, '00' to '59'
%S      Second, '00' to '59'
%I      Hour (12-hour clock), '01' to '12'

%p      'AM' or 'PM'
%B      Full month name, as in 'November'
%b      Abbreviated month name, as in 'Nov'
%j      Day of the year, '001' to '366'
%w      Day of the week, '0' (Sunday) to '6' (Saturday)
%A      Full weekday name, as in 'Monday'
%a      Abbreviated weekday name, as in 'Mon'
"""

import datetime
import time
import inspect

def now_time(format='%H:%M:%S'):
    return datetime.datetime.now().time().strftime(format)

def now_time_unix():
    return time.time()

def now_datetime(format='%Y-%m-%d %H:%M:%S'):
    return to_date_string(datetime.datetime.now(), format)


def to_date_string(dt, format='%Y-%m-%d %H:%M:%S'):
    return dt.strftime(format)

def to_time_string(dt, format='%H:%M:%S'):
    #%I:%M %p  12hour:min pm
    return dt.strftime(format)

def to_datetime(dt_str=None, format='%Y-%m-%d %H:%M:%S'):
    if not dt_str:
        return datetime.datetime.now()
    return datetime.datetime.strptime(dt_str, format)

def to_date(dt_str, format='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.strptime(dt_str, format).date()

def to_time(dt_str, format='%Y-%m-%d %H:%M:%S'):
    parsed = datetime.datetime.strptime(dt_str, format).time()
    return parsed

def __add(dt, **unit):
    val = list(unit.values())[0]
    delta = datetime.timedelta.__call__(**unit)
    #print(delta)
    if val>0:
        return dt+delta
    else:
        return dt-delta

def add_day(datetime_obj, day):
    return __add(datetime_obj, days=day)

def add_hour(time_obj, hour):
    return __add(time_obj, hours=hour)
def add_minute(time_obj, minute):
    return __add(time_obj, minutes=minute)
def add_second(time_obj, second):
    return __add(time_obj, seconds=second)

def diff_in_second(dt1, dt2):
    diff = dt1-dt2
    total_seconds= diff.days*24*3600+diff.seconds

def diff(dt1,dt2):
    return dt1-dt2
