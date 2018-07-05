# coding: utf-8

#データフレームのカラムからの抽出クラス
import pandas as pd
import numpy as np
from math import log10, floor

class DFex:
    def stw(self, df, prefix=list, drop=0):
        if type(prefix)==str: prefix=[prefix]
        new_index=[]
        for i in prefix:
            new_index.extend(df.columns[df.columns.str.startswith(i)])
        if drop==0:
            new_df=df.loc[:, new_index]
        elif drop==1:
            new_df=df.drop(new_index, axis=1)
        return new_df
    
    def enw(self, df, suffix=list, drop=0):
        if type(suffix)==str: suffix=[suffix]
        new_index=[]
        for i in suffix:
            new_index.extend(df.columns[df.columns.str.endswith(i)])
        if drop==0:
            new_df=df.loc[:, new_index]
        elif drop==1:
            new_df=df.drop(new_index, axis=1)
        return new_df
    
    def cont(self, df, fix=list, drop=0):
        if type(fix)==str: fix=[fix]
        new_index=[]
        for i in fix:
            new_index.extend(df.columns[df.columns.str.contains(i)])
        if drop==0: new_df=df.loc[:, new_index]
        elif drop==1: new_df=df.drop(new_index, axis=1)
        return new_df
    


#date time型への変換
class Convert_DateTime():
    def convert_date(self, st_time):
        ref_time=pd.datetime.date(pd.to_datetime(st_time))
        return ref_time

    def convert_time(self, st_time):
        ref_time=pd.datetime.time(pd.to_datetime(st_time))
        return ref_time
    
### 有効数字を揃える
class SignificantFigure():
    def round_sig(self, x, sig=2):
        data=np.around(x, sig-int(floor(log10(abs(x))))-1)
        return data
