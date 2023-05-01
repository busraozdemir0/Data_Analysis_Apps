# --- Pandas DataFrame ile filtreleme işlemleri ---

import pandas as pd
import numpy as np

data=np.random.randint(10,100,75).reshape(15,5) # 15'e 5'lik seri tanımladık
df=pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])

result=df
resukt=df.columns # dataframe'deki kolon adları gelir
result=df.head() # ilk 5 satır gelir
result=df.head(10) # ilk 10 satır gelir
result=df.tail() # son 5 satır gelir
result=df.tail(8) # son 8 satır gelir
result=df["Column1"].head() # Column1'in ilk 5 kaydını alır
result=df.Column1.head() # bir üstteki satırla aynı sonucu verir, alternatif yöntemdir.
result=df[["Column1","Column2"]].head() # Column1 ve Column'nin ilk 5 kaydı gelir
result=df[5:15][["Column1","Column2"]].head() # ikinci 5 satırı alır


# filtreleme işlemi

result=df>50 # 50 'den büyükler için True gelir
result=df[df>50] # 50'den büyük kayıtları gösterir 50'den küçük kayıtlar için de NaN yazar
result=df[df%2==0] # çift olan kayıtları gösterir, tek kayıtlar için NaN ifadesi yazar
result=df[df["Column1"]>50][["Column1","Column2"]] # Column1 üzerinden 50'den büyük olan kayıtları sadece Column1 ve Column'yi listeleyecek şekilde getirir
result=df[(df["Column1"]>50) & (df["Column1"]<=70)] # Column1 için 50'den büyük olması ve 70'ten küçük eşit olması gerektiğini belirten filtreleme 
result=df[(df["Column1"]>50) | (df["Column2"]>50)][["Column1","Column2"]] # or işareti olduğu için içlerinden bir tanesi sağlansa yeterli
result=df.query("Column1>=50 & Column1 % 2==0") # Column1'in hem 50den büyük eşit hem de çift olması gerektiğini bildiren sorgu ifadesi
result=df.query("Column1>=50 | Column1 % 2==0")[["Column1","Column2"]]



print(result)