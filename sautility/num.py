# -*- coding: utf-8 -*-
'''Number utility module'''
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR, ROUND_CEILING


def n2d(value) -> Decimal:
    '''数値(int,float)をDecimal型へ変換'''
    try:
        return Decimal(str(value))
    except:
        return None


def dround(src_value: Decimal, precision) -> Decimal:
    '''四捨五入 for Decimal'''
    try:
        return src_value.quantize(Decimal(str(precision)), rounding=ROUND_HALF_UP)
    except:
        return None


def dfloor(src_value: Decimal, precision) -> Decimal:
    '''切り捨て for Decimal'''
    try:
        return src_value.quantize(Decimal(str(precision)), rounding=ROUND_FLOOR)
    except:
        return None


def dceiling(src_value: Decimal, precision) -> Decimal:
    '''切り上げ for Decimal'''
    try:
        return src_value.quantize(Decimal(str(precision)), rounding=ROUND_CEILING)
    except:
        return None
