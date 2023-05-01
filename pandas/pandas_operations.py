# --- Pandas ile DataFrame metotları ---

import pandas as pd
import numpy as np

data={
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcad","ade","cb","dea"]
}

df=pd.DataFrame(data)

def kareal(x):
    return x*x

kareal2= lambda x: x*x

result=df
result=df["Column2"].unique() # verileri tekrarlanmayan şekilde listeler.
result=df["Column2"].nunique() # 4 tane tekil bilgi olduğu için 4 sayısı gelir.
result=df["Column2"].value_counts() # her bir elemanın kaçar defa tekrar ettiği sayısını bize verir.
result=df["Column1"]*2 # column1'deki elemanlar tek tek 2 ile çarpılır
result=df["Column1"].apply(kareal) # apply ile kareal adlı fonksiyona giderek Column1'deki her bir elemanın karesini almasını sağlıyoruz.
result=df["Column1"].apply(kareal2) # yukarıdaki satır ile aynı işi yapar.
result=df["Column1"].apply(lambda x: x*x) # yukarıdaki satır ile aynı işi yapar.
result=df["Column3"].apply(len) # Column3 içerisinde her bir elemanın kaç karakterli olduğu bilgisini verir.
df["Column4"]=df["Column3"].apply(len) # Column3 içerisindeki elemanların karakter sayılarını Column4 adlı kolon oluşturarak içerisine yazar.
result=len(df.columns) # 4
result=len(df.index) # 5 (satır)

result=df.sort_values("Column2") # Column2'deki elemanları sıralar.
result=df.sort_values("Column3") # Column3'deki elemanları alfabetik (artan) sıralar.
result=df.sort_values("Column3",ascending=False) # Column3'deki elemanları alfabetik (azalan şekilde) sıralar.

print(result) 

data2={
    "Ay":["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap"],
    "Gelir":[20,30,15,14,32,42,12,36,52]
}

df=pd.DataFrame(data2)
print(df.pivot_table(index="Ay",columns="Kategori",values="Gelir")) # data2'de yer alan verileri kendimiz kolon Kategori ve indexler Ay olacak şekilde pivot tablo elde ettik.


