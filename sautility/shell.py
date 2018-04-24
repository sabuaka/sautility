# -*- coding: utf-8 -*-
import sys
import os

def isccbreak(key):
    """getchで取得したキーがCtrl+Cであるかを判定します"""
    CTRL_C = 3
    if ord(key) == CTRL_C:
        return True
    else:
        pass
    return False

def clear():
    """コンソールをクリアします"""
    os.system('cls' if os.name=='nt' else 'clear')

def getch():
    """キー入力を待ち入力されたキーを返します（inputとは異なりエンターを待ちません）"""
    if sys.platform == 'win32':
        from msvcrt import getch as lcgetch
    else:
        def lcgetch():
            import tty
            import termios
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                return sys.stdin.read(1).encode('utf-8')
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
    
    return lcgetch()
