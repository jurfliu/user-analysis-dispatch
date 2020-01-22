# -*- coding: utf-8 -*-

# @File    : read_bike_info.py
# @Date    :  2020-01-22 15:46
# @Author  : admin

import pandas as pd
pr = pd.read_csv("../data/order_bike2.csv",encoding='unicode_escape');
print(pr.info())
print(pr.shape)

#jurfliu  123456_ljf