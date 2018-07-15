# -*- coding: utf-8 -*-
'''Shell utility module'''
import sys
import os
import tty
import fcntl
import termios
import builtins as __builtin__


def print(*args, **kwargs):  # override pylint: disable-msg=W0622
    '''override print'''
    kwargs['end'] = '\r\n'
    return __builtin__.print(*args, **kwargs)


def isccbreak(key):
    """getchで取得したキーがCtrl+Cであるかを判定します"""
    if key is None or len(key) <= 0:
        return False

    CTRL_C = 3   # 可読性を優先 pylint: disable-msg=C0103
    if ord(key) == CTRL_C:
        return True
    else:
        pass
    return False


def clear():
    """コンソールをクリアします"""
    os.system('cls' if os.name == 'nt' else 'clear')


def getch():
    '''Wait for key input and returns inputed key (bytes type)'''
    fd = sys.stdin.fileno()  # 可読性を優先 pylint: disable-msg=C0103
    old = termios.tcgetattr(fd)
    in_key = 0
    try:
        tty.setraw(fd)
        in_key = sys.stdin.read(1).encode('utf-8')
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return in_key


def nb_getch():
    '''(nonblock)Monitoring key input.'''
    # get current preferences
    fno = sys.stdin.fileno()
    org_attr = termios.tcgetattr(fno)
    org_fcntl = fcntl.fcntl(fno, fcntl.F_GETFL)

    # Temporarily exclude "icanon" from attribute of shell.
    attr = termios.tcgetattr(fno)
    attr[3] &= ~termios.ICANON
    termios.tcsetattr(fno, termios.TCSADRAIN, attr)

    # Temporarily set stdin to "NONBLOCK".
    fcntl.fcntl(fno, fcntl.F_SETFL, org_fcntl | os.O_NONBLOCK)

    # Monitoring key input
    in_key = 0
    try:
        in_key = sys.stdin.read(1).encode('utf-8')
    finally:
        # set back original preferences.
        fcntl.fcntl(fno, fcntl.F_SETFL, org_fcntl)
        termios.tcsetattr(fno, termios.TCSANOW, org_attr)
    return in_key
