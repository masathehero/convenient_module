# coding: utf-8
import re
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

    def split_str_num(self, data, top_industry=1000):
        '''
        データフレームの文字と数字を切り分ける
        '''
        pattern_int=r'([0-9]+$)'
        pattern_str=r'([^0-9]+)'
        number=[]
        comp_name=[]
        data=data.dropna()
        dummy=data.applymap(lambda x: number.append(int(re.findall(pattern_int, x)[0])))
        dummy=data.applymap(lambda x: comp_name.append(re.findall(pattern_str, x)[0][:-1]))
        splited_data=pd.concat([pd.Series(comp_name), pd.Series(number)], axis=1).drop_duplicates()##このdrop_duplicateちょっと危険かも
        return splited_data 


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
