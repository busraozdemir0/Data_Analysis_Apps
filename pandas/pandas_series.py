# --- Pandas Serileri ---
#numpy'da daha çok sayısal veriler üzerinde çalıştık
#pandas'da ise her türlü veriler üzerinde çalışacağız

import pandas as pd
import numpy as np

# data
numbers=[20,30,40,50]
letters=['a','b','c','d',20] #her bir eleman aynı tipte olmak zorunda değil
dict={"a":10,"b":20,"c":30,"d":40}
random_numbers=np.random.randint(10,100,6)

# pandas_series=pd.Series()
pandas_series=pd.Series(numbers) #elemanları alt alta yazdırır elemanların başına da index numaralarını otomatik yazdırır
pandas_series=pd.Series(letters) 
pandas_series=pd.Series(5) # 0    5
pandas_series=pd.Series(5,[0,1,2,3]) #kendimiz 4 tane index numarası verdiğimiz için 4 kere alt alta index numaralarıyla birlikte 5 yazdırılır
pandas_series=pd.Series(numbers,['a','b','c','d']) # ['a','b','c','d'] buradaki key bilgileriyle eşleştirilecek
pandas_series=pd.Series(dict)
pandas_series=pd.Series(random_numbers)


pandas_series=pd.Series([20,30,40,51],['a','b','c','d'])
result=pandas_series[0] #indexleri a,b,c,d olarak değiştirsek bile 0.indexe ulaştığımızda 20 bilgisi gelecektir
result=pandas_series[:2] #ilk 2 eleman
result=pandas_series[-2:] #son 2 eleman
result=pandas_series["b"] #30
result=pandas_series[["a","c"]] #20 40
result=pandas_series.ndim #kaç boyutlu olduğu bilgisi => 1
result=pandas_series.dtype #data type
result=pandas_series.shape
result=pandas_series.sum() #elemanları toplamı
result=pandas_series.max() #en büyük eleman
result=pandas_series+pandas_series #iki elemanlar toplanır
result=pandas_series+50 #her eleman üzerine 50 sayısı eklenir
result=np.sqrt(pandas_series)

result=pandas_series >= 50 #50den küçükse false 50den büyük eşitse true değeri döner
result=pandas_series % 2 == 0

print(pandas_series[pandas_series % 2 == 0]) #sadece çift sayıları getir

print(pandas_series)
print(result)

# basic example

opel2018=pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019=pd.Series([40,30,20,10],["astra","corsa","grandland","insignia"])

total=opel2018+opel2019
print(total) # astra        60.0 -- opel2018 de ve opel2019 'da aynı değişkenlere karşılık gelen alanları topladı. örneğin astra:20+ astra: 40
             # corsa        60.0
             # grandland     NaN -- grandland'ın opel2018'de karşılığı olmadığı için NaN ifadesi geldi
             # insignia     20.0
             # mokka         NaN
print(total["astra"]) #60.0