# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:56:19 2021

@author: wricw
"""

import csv

with open('members.csv') as csv_file:
    members = csv.DictReader(csv_file, delimiter=',')
    result = {}
    for row in members:
        print(row)

