# --- IMDB Filmlerinin Veri Analizi ---

# *** imdb.csv dosyasını şu linkten üye olarak indirebilirsiniz => https://data.world/

import pandas as pd

df=pd.read_csv("pandas/datasets/imdb.csv")

# 1- Dosya hakkındaki bilgiler.

result=df
result=df.columns # kolon adları gelir
result=df.info # dataframe hakkında bilgi

# 2- İlk 5 kaydı gösterin.

result=df.head()

# 3- İlk 10 kaydı gösterin.

result=df.head(10)

# 4- Son 5 kaydı gösterin.

result=df.tail()

# 5- Son 10 kaydı gösterin

result=df.tail(10)

# 6- Sadece Title kolonunu alın

result=df["Title"]

# 7- Sadece Title kolonunu içeren ilk 5 kaydı alın

result=df["Title"].head()

# 8- Sadece Title ve Rated kolonunu içeren ilk 5 kaydı alın.

result=df[["Title","Rated"]].head()

# 9- Sadece Title ve Rated kolonunu içeren son 7 kaydı alın.

result=df[["Title","Rated"]].tail(7)

# 10- Sadece Title ve Rated kolonunu içeren ikinci 5 kaydı alın.

result=df[5:][["Title","Rated"]].head()
# * result=df[5:10][["Title","Rated"]]

# 11- Sadece Title ve Rated kolonunu içeren ve imdb puanı 2.5 ve üstünde olan kayıtlardan ilk 50 tanesini alın.

result=df[df["imdbRating"]>=2.5][["Title","Rated"]].head(50)

# 12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.

result=df[(df["Released"] >= "2014") & (df["Released"] <= "2015")][["Title","Released"]]

# 13- Değerlendirme sayısı(Metascore) 15.0'dan büyük ya da imdb puanı 2.5 ile 3 arasında olan filmleri listeleyiniz.

result=df[(df["Metascore"]>=18.0) | ((df["imdbRating"]>=2.5)  & (df["imdbRating"]<=3.0))][["Title","imdbRating","Metascore"]]


print(result)