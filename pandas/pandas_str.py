# --- Pandas ile String fonksiyonları ----
# örnek csv dosyalarını https://www.kaggle.com/ sitesine üye olarak indirebilirsiniz.

import pandas as pd

data=pd.read_csv("pandas/datasets/all_seasons.csv")

data.dropna(inplace=True) # inplace=True kullanarak NaN verileri sildiğimizde orijinal df'ye yansıması için yapıldı.

data["team_abbreviation"]=data["team_abbreviation"].str.lower() # belirtilen alanların hepsini küçük harfe çevirdik.
data["index"]=data["player_name"].str.find("a") # a karakterini player_name içerisinde arar ve index adlı kolon oluşturarak bulunduğu indeksi yazar
data=data[data["college"].str.contains("Florida")] # içerisinde Florida geçen kayıtları getirir.
data=data["player_name"].str.replace(" ","-") #player_name içerisinde yer alan boşluk karakterleri yerine - ekler.

# player_name'de boşluk karakterinden ayırarak FirstName ve LastName adlı kolon oluşturup isim ve soyisimleri oraya yazar
# data[["FirstName","LastName"]]=data["player_name"].loc[data["player_name"].str.split().str.len()==2].str.split(expand=True)

print(data.head(10))

