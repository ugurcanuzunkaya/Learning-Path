# -*- coding: utf-8 -*-
"""12527708710_Uğurcan_Uzunkaya_HW2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wsqjmxphjqnMtR2OWHzLxRGuxnpzUAyZ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bronz_df = pd.read_excel('bronz.xlsx')
gumus_df = pd.read_excel('gumus.xlsx')
altin_df = pd.read_excel('altin.xlsx')
insani_gelisim_indeksi_df = pd.read_excel('insani_gelisim_indeksi.xlsx')

bronz_gumus_df = pd.merge(bronz_df, gumus_df, how="outer", on="Country", suffixes=["_Bronz", "_Gumus"])
bronz_gumus_altin_df = pd.merge(altin_df, bronz_gumus_df, how="outer", on="Country", suffixes=["_Altin", "_Medals"])
bronz_gumus_altin_df = bronz_gumus_altin_df.replace(np.nan, 0)
madalya_df = bronz_gumus_altin_df.drop(labels=["NOC_Bronz", "NOC_Gumus"], axis=1)
madalya_df["Total_Medals"] = madalya_df.sum(axis=1)
print(madalya_df)

df_madalya = madalya_df.rename(
    columns={"Country": "Ulke", "Total": "Altin", "Total_Bronz": "Bronz", "Total_Gumus": "Gumus",
             "Total_Medals": "Toplam"})
print(df_madalya)

df_ulkeler = pd.merge(madalya_df, insani_gelisim_indeksi_df, how="inner", on="Country")
df_ulkeler = df_ulkeler.rename(
    columns={"Country": "Ulke", "Total": "Altin", "Total_Bronz": "Bronz", "Total_Gumus": "Gumus",
             "Total_Medals": "Toplam", "2008_Human Development Index": "2008_Insani Gelisim Indeksi"})
print(df_ulkeler)

plt.scatter(df_ulkeler["Toplam"], df_ulkeler["2008_Insani Gelisim Indeksi"], marker="*", color="blue")
plt.xlabel("Toplam Madalya Sayisi")
plt.ylabel("2008 Insani Gelisim Indeksi")
plt.title("Ulkelerin Insani Gelisim Endeksinin Toplam Madalya Sayisina gore Dagilim Grafigi")
plt.show()

df_ulkeler_up_09 = df_ulkeler.loc[df_ulkeler["2008_Insani Gelisim Indeksi"] >= 0.9]
plt.bar(df_ulkeler_up_09["Ulke"], df_ulkeler_up_09["Toplam"], color="red", width=0.3)
plt.bar(df_ulkeler_up_09["Ulke"], df_ulkeler_up_09["Altin"], color="blue", width=0.3)
plt.ylabel("Madalya Sayisi")
plt.xlabel("Ulke Isimleri")
plt.xticks(rotation="vertical")
plt.title("Insani Gelisim Indeksi 0.9 Uzeri Olan Ulkelerin Altın ve Toplam Madalya Sayıları Grafigi")
plt.show()
