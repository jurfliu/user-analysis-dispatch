#!usr/bin/env python
#-*- coding:utf-8 _*-
'''
@author:Administrator
@file: box_demo.py
@time: 2020-01-18 下午 4:30
https://segmentfault.com/a/1190000015926584   异常值检测
'''
import pandas as pd
import matplotlib.pyplot as plt


def programmer_1(file_name):
    catering_sale = file_name
    data = pd.read_excel(catering_sale, index_col=u'日期')
    print(data)

    # windows下设置字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure()
    # 画箱线图
    p = data.boxplot(return_type='dict')
    x = p['fliers'][0].get_xdata()
    y = p['fliers'][0].get_ydata();
    y.sort();
    print(x)
    print(y)
    #以下参数都是经过调试的，需要具体问题具体调试
    for i in range(len(x)):
        # 处理临界情况， i》0时
        if i>0:
            plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i] +0.05-0.8 / (y[i] - y[i - 1]), y[i]))
        else:
            plt.annotate(y[i],xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))
    plt.show()
path="../data/catering_sale.xls";
programmer_1(path);

