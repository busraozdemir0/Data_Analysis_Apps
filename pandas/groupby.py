# --- Pandas DataFrame ile GroupBy kullanımı ---

import pandas as pd
import numpy as np

personeller = {
    "Çalışan": ["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz"],
    "Departman":["İnsan Kaynakları","Bilgi işlem","Muhasebe","İnsan Kaynakları"],
    "Yaş":[30,25,45,50],
    "Semt":["Kadıköy","Tuzla","Maltepe","Tuzla"],
    "Maaş":[5000,3000,4000,3500]
}

df=pd.DataFrame(personeller)
result=df
result=df["Maaş"].sum()
result=df.groupby("Departman").groups
result=df.groupby(["Departman","Semt"]).groups # Hem departmana hem de semte göre gruplama işlemi.

 
# semte göre gruplama yapıyoruz.
for name,group in df.groupby("Semt"):
    print(name)
    print(group)

# departmana göre gruplama işlemi.
for name,group in df.groupby("Departman"):
    print(name)
    print(group)

result=df.groupby("Semt").get_group("Tuzla") #Tuzla'da oturan kişileri aldık.
result=df.groupby("Departman").get_group("İnsan Kaynakları")
result=df.groupby("Departman").mean() # departmana göre gruplanarak yaş ve maaş ortalamaları gelir.
result=df.groupby("Departman")["Maaş"].mean() # Departmana göre Maaş ortalamaları hesaplanıp yazdırılacak.
result=df.groupby("Semt")["Yaş"].mean() # Semtlere göre yaş ortalamalarını verir.
result=df.groupby("Semt")["Çalışan"].count() # Semtlere göre çalışan kişi sayısını verir.
result=df.groupby("Departman")["Yaş"].max() 
result=df.groupby("Departman")["Maaş"].max()["İnsan Kaynakları"] # İnsan Kaynakları departmanında max maaş bilgisini getirir.
result=df.groupby("Departman").agg(np.mean) # Departmana göre yaş ve maaş ortalamasını numpy üzerinden agg fonksiyonu ile yaptık.
result=df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]) # numpy ile departmanlara göre maaşların toplamları, ortalaması, max ve min değerleri gelir.
result=df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["İnsan Kaynakları"] # İnsan Kaynakları alanına göre maaşların toplamları, ortalaması, max ve min değerleri gelir.


print(result)