#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 13:22:07 2022

@author: y56
"""

import os
import csv
import shutil


pwd  = '/home/y56/Downloads/png-2022-07-19T11-37/out_scv011-dsv-001_png/'

fli = os.listdir('out_scv011-dsv-001_png')

keyword_li = []
with open('need-to-check', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        keyword_li.append(row[0])


for f in fli:
    for x in keyword_li:
        if x in f:
            print(pwd + f)
            shutil.copyfile(pwd + f, './'+f)
