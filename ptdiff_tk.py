#!/usr/bin/env python
"""
"""

import sys

import ui.mainwindow
from ui.mainwindow import MainWindow

import puren_tonbo


print('try monkey patch')
ui.mainwindow.open = puren_tonbo.pt_open
# TODO set password caching too, use tk to match this GUI!
# also don't have it prompt twice if same password is used


# Yep, no error checking
leftpath = sys.argv[1]
rightpath = sys.argv[2]

main_window = MainWindow()
main_window.start(leftpath, rightpath)
