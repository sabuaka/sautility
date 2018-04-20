# -*- coding: utf-8 -*-
import datetime

def get_dt_short():
    """現在の日時を文字列(YYYYMMDDHHMMSS)で返す"""
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def get_dt_long():
    """現在の日時を文字列(YYYY/MM/DD HH/MM/SS.f)で返す"""
    return datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')

def get_uts_s():
    """unix timestamp を整数(秒)で取得"""
    now = datetime.datetime.now()
    ut_s = int(now.timestamp())
    return ut_s

def get_uts_ms():
    """unix timestamp を整数(ミリ秒)で取得"""
    now = datetime.datetime.now()
    ut_ms = int(now.timestamp() * 1000) # s to ms
    return ut_ms

def get_timestamp():
    """unix timestamp をfloatでマイクロ秒まで取得"""
    return datetime.datetime.now().timestamp()

