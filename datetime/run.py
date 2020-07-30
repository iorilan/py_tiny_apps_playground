import datetime_helper as helper

if __name__ == "__main__":
    print(f'========now time ======')
    print(helper.now_time())
    print(helper.now_time_unix())
    print(helper.now_datetime())

    print('==========str to date============')
    dt1='2020-02-01 12:50:11'
    dt1_obj = helper.to_datetime(dt1)
    print(dt1_obj)
    print(helper.to_date(dt1))
    print(helper.to_time(dt1))

    print('===add days 2====')
    dt1_obj=helper.add_day(dt1_obj,2)

    print(helper.to_date_string(dt1_obj))

    print('===add hour -4====')
    dt1_obj=helper.add_hour(dt1_obj,-4)
    print(helper.to_date_string(dt1_obj))

    print('===add mins 58====')
    dt1_obj=helper.add_minute(dt1_obj,58)
    print(helper.to_date_string(dt1_obj))

    print('===add second 50====')
    dt1_obj=helper.add_second(dt1_obj,50)
    print(helper.to_date_string(dt1_obj))

    print('===compare date====')
    dt1=helper.to_datetime('2020-05-01 11:50:30')
    dt2=helper.to_datetime('2020-06-02 10:50:20')
    print(helper.diff_in_second(dt2,dt1))
    
    