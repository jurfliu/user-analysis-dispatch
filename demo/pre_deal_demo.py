#!usr/bin/env python
#-*- coding:utf-8 _*-
'''
@author:Administrator
@file: pre_deal_demo.py
@time: 2020-01-18 上午 11:05
'''
import os
import pandas as pd
from scipy.interpolate import lagrange
#拉格朗日插值代码，index插入的位置，df为列向量，k为取前后的个数
def deal_empty_column(index, df, k=5):
    print(index)
    #取插补值索引前，后各5个数
    y = df[list(range(index - k, index))
           + list(range(index + 1, index + 1 + k))]
    y = y[y.notnull()]
    #调用拉格朗日插值函数
    return lagrange(y.index, list(y))(index)
#处理确实值
def deal_null_val():
    path = os.getcwd();
    print(path)
    inputfile = path + '/data/catering_sale.xls'
    #outputfile = path + '../data/catering_sale_out.xls'
    outputfile = 'd:/catering_sale_out.xls'
    df = pd.read_excel("../data/catering_sale.xls")
    df2 = pd.read_excel("../data/catering_sale.xls")
    data=df;
    print(data,df)
    data[(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None
    #对data 修改，df也同样被修改了
    print(data, df)
    data_temp = data[data[u'销量'].isnull()]
    index_list = data_temp[u'销量'].index
    print(index_list)
    for index in index_list:
        v=deal_empty_column(index, data[u'销量']);
        print("v",v);
        #data[u'销量'][index] = deal_empty_column(index, data[u'销量'])
        df2.loc[index,u'销量']=v;
    print(df2);
    df2.to_excel(outputfile)
#调用
deal_null_val();