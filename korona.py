# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:56:00 2020

@author: elifb
"""

import pandas as pd

import matplotlib.pyplot as plt

df1 = pd.read_excel("Koronalı günler 2020.xlsx")

df2 = pd.read_excel("Koronasız günler 2018.xlsx")


print(df1.columns)

print(df1.info())

print(df1.describe())

dfkoronalırize = df1.drop(["Tarih"],axis=1) #Tarih bilgisi df1'den çıkarıldı.
dfkoronasızrize = df2.drop(["Tarih"],axis=1) #Tarih bilgisi df2'den çıkarıldı.

dfkoronalırize.plot(grid=True)
plt.show()

dfkoronasızrize.plot(grid=True)
plt.show()





