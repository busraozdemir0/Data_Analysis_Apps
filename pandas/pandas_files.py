# örnek csv json uzantılı veri setlerini aşağıdaki linkten üye olarak indirebiliriz.
#  https://www.kaggle.com/datasets/

import sqlite3 #sqlite'dan veri çekmek için
import pandas as pd

df=pd.read_csv("pandas/datasets/sample.csv") # dizindeki csv dosyasını okuduk
df=pd.read_json("pandas/datasets/sample.json",encoding="utf-8")
df=pd.read_excel("pandas/datasets/sample.xlsx") #excel dosyasını okuyabilmek için şu kütüphane indirilmeli => pip install xlrd

#veritabanından bilgi çekmek
#sqlite ile verileri çekmek istersek => pip install pysqlite3

# connection=sqlite3.connect("sample.db")
# df=pd.read_sql_query("SELECT * FROM students",connection)

print(df)