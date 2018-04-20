# -*- coding: utf-8 -*-
from decimal import Decimal

def n2d(value) -> Decimal:
    '''数値(int,float)をDecimal型へ変換'''
    return Decimal(str(value))
