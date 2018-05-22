# -*- coding: utf-8 -*-
'''Number utility module'''
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR


def n2d(value) -> Decimal:
    '''数値(int,float)をDecimal型へ変換'''
    return Decimal(str(value))


def dround(src_value: Decimal, precision) -> Decimal:
    '''四捨五入 for Decimal'''
    return src_value.quantize(Decimal(str(precision)), rounding=ROUND_HALF_UP)


def dfloor(src_value: Decimal, precision) -> Decimal:
    '''切り捨て for Decimal'''
    return src_value.quantize(Decimal(str(precision)), rounding=ROUND_FLOOR)
