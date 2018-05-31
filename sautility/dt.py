# -*- coding: utf-8 -*-
'''date time utility module'''
from datetime import datetime

DT_STR_FORMAT = '%Y-%m-%d %H:%M:%S'


def get_hour():
    '''現在時刻の時をintで取得'''
    return int(datetime.now().strftime('%H'))


def get_minute():
    '''現在時刻の分をintで取得'''
    return int(datetime.now().strftime('%M'))


def get_dt_short():
    '''現在の日時を文字列(YYYYMMDDHHMMSS)で返す'''
    return datetime.now().strftime('%Y%m%d%H%M%S')


def get_dt_long():
    '''現在の日時を文字列(YYYY/MM/DD HH/MM/SS.f)で返す'''
    return datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')


def get_uts_s():
    '''unix timestamp を整数(秒)で取得'''
    now = datetime.now()
    ut_s = int(now.timestamp())
    return ut_s


def get_uts_ms():
    '''unix timestamp を整数(ミリ秒)で取得'''
    now = datetime.now()
    ut_ms = int(now.timestamp() * 1000)  # s to ms
    return ut_ms


def get_timestamp():
    '''unix timestamp をfloatでマイクロ秒まで取得'''
    return datetime.now().timestamp()


def dt2str(dt) -> str:
    '''convert from datetime type to string type'''
    try:
        if isinstance(dt, datetime):
            return dt.strftime(DT_STR_FORMAT)
        return str(None)
    except:
        return str(None)


def str2dt(dt_str) -> datetime:
    '''convert from datetime type to string type'''
    try:
        return datetime.strptime(dt_str, DT_STR_FORMAT)
    except:
        return str(None)
