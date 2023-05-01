# --- Pandas ile Kayıp ve Bozuk Veri Analizi ---
# ** Kayıp ve bozuk verilerle nasıl çalışabiliriz? => (değeri NaN olan veriler)

import pandas as pd
import numpy as np

data=np.random.randint(10,100,15).reshape(5,3)

df=pd.DataFrame(data,index=["a","c","e","f","h"],columns=["column1","column2","column3"])

df=df.reindex(["a","b","c","d","e","f","g","h"]) # yeniden indeksleme yaptık

newColumn=[np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"]=newColumn # column4 oluşturduk ve newColumn değerlerini 4. kolona aktarmış olduk

result=df
result=df.drop("column1",axis=1) # axis değerine 1 verdiğimiz için kolona karşılık gelir. Eğer 0 verseydik satıra karşılık gelecekti.
result=df.drop(["column1","column2"],axis=1)  # column1 ve column2 silinir
result=df.drop("a",axis=0) # a indexini silmek istediğimiz için satıra karşılık gelecek olan axis'i 0 yaptık.
result=df.drop(["a","b","h"],axis=0) # a, b ,h indexleri silinir.

# NaN (Not a Number) olan alanları tespit etme
result=df.isnull() # NaN olan alanlar için True değeri döner, diğerleri için False
result=df.notnull() # NaN olan alanlar için False değeri döner, diğerleri için True (isnull'un tam tersi)
result=df.isnull().sum() # değeri null olan alanları sayar
result=df["column1"].isnull().sum() # column1'deki null ifadeleri sayar
result=df[df["column1"].isnull()]["column1"] # column1'de NaN olan kayıtlar gelir
result=df[df["column1"].notnull()]["column1"] # column1'de değeri olanlar karşımıza gelir. Yani null olmayanlarla ilgileneceksek notnull kullanılır.

result=df.dropna() # varsayılan axis=0'dır yani satıra göre silecektir. NaN değerleri silmek için dropna() fonksiyonu kullanılır.
result=df.dropna(axis=1) # sütuna göre NaN değerleri silecektir. NaN değeri bir tane olsa bile komple o sütunu silecektir.
result=df.dropna(how="any") # bir tane bile NaN ifadesi bulursa siler.
result=df.dropna(how="all") # tüm satır NaN ise o satırı siler.
result=df.dropna(subset=["column1","column2"],how="all") # column1 ve column2'yi dikkate alarak kolonda tüm değerler NaN ise siler.
result=df.dropna(subset=["column1","column2"],how="any") # column1 ve column2'yi dikkate alarak kolonda bir tane bile NaN var ise siler.
result=df.dropna(thresh=2) # en az iki tanesinin değeri varsa yani normal veriyse silmez.
result=df.dropna(thresh=4) # en az dört tanesinin değeri varsa yani normal veriyse silmez.

result=df.fillna(value="no input") # fillna metodu ile NaN değerleri 'no input' ile dolduracak.
result=df.fillna(value=1)

result=df.sum()
result=df.sum().sum() # df'deki toplam sayısal değerin sonucunu verir.
result=df.size # eleman sayısı gelir
result=df.isnull().sum().sum() # df'de yer alan toplam NaN değerlerin sayısını verir

def ortalama(df):
    toplam=df.sum().sum()
    adet=df.size - df.isnull().sum().sum()
    return toplam/adet

result=df.fillna(value=ortalama(df)) # NaN değerler yerine hesaplanan ortalama değer yazdırılmış oldu.

print(result)