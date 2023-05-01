# --- Pandas DataFrame ile Satır ve Sütun Seçimleri ---

import pandas as pd
from numpy.random import randn
df=pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])

result=df
result=df["Column1"]
result=type(df["Column1"]) # Series
result=df[["Column1","Column2"]] #iki kolonlu dataframe bize gönderilir

#satıra göre seçme
# loc["row","column"] => loc["row"] => loc[":","column"]
result=df.loc["A"]
result=type(df.loc["A"]) # Series
result=df.iloc[2] # indexle çalışmak istiyorsak iloc kullanılır

result=df.loc[:,"Column1"] #sadece kolon1 gelir
result=df.loc[:,["Column1","Column2"]] #satır seçmek istemediğimiz için iki nokta (:) ile başladık
result=df.loc[:,"Column1":"Column3"] # kolon1'den kolon3'e kadar hepsini getirir (başlangıç ve bitişler dahildir)
result=df.loc[:,:"Column2"] # (başlangıç belirtmedik) kolon1 ve kolon2 gelir 
result=df.loc["A":"B":,:"Column2"] # sadece A, B satırlarını ve kolon olarak da sadece Column1 ve Column2 gelir
result=df.loc[:"B":,:"Column2"] # A ve B satırları
result=df.loc["A","Column2"] # A'nıncı satırın Column'ye karşılık gelen değeri
result=df.loc["C","Column1"]
result=df.loc[["A","B"],["Column1","Column2"]] # A ve B satırlarının Column1 ve Column2'ye karşılık gelen değerleri

# kolon eklemek istersek;
df["Column4"]=pd.Series(randn(3),["A","B","C"]) # 4. kolon eklendi
df["Column5"]=df["Column1"]+df["Column3"] # Column1 ile Column3'ün toplamı Column5 olarak yazdırıldı

# kolon silmek istersek
result=df.drop("Column5",axis=1, inplace=True) # axis=1 => Column5'i yukarıdan aşağıya sil anlamında,  inplace=True => dataframe'in orijinalini değiştirmek için

print(result)
print(df)