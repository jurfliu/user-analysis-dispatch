# -*- coding: utf-8 -*-

# @File    : d.py
# @Date    :  2020-01-21 18:28
# @Author  : admin



import  numpy as np;
def standDeal():
    x_train = np.array([[4, 4, 6,8,1], [6, 6, 22,19,0], [27, 23, 4,3,2]])
    data=x_train;

    print((data - data.mean()) / data.std())#执行零-均值规范化
