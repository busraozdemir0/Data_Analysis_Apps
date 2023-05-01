# --- Python'da Pandas ile DataFrame tanımlamaları ---
# DataFrame ile basit bir tablo görünümü gibi yapılabilir. => kolon başlıkları ve satır başlıkları(index) olduğu için

import pandas as pd

# s1=pd.Series([3,2,0,1])
# s2=pd.Series([0,3,7,2])

# data=dict(apples=s1,oranges=s2) # burada yer alan apples ve oranges kolon başlığı olarak yer alır. Eğer kolon ismi verilmeden yazdırılırsa otomatik 0 ve 1 yazar

# df=pd.DataFrame(data)

# print(df)


data=[["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]
dict={"Name": ["Ahmet","Ali","Yağmur","Çınar"],"Grade":[50,60,70,80]}
dict_list=[
            {"Name":"Ahmet","Grade":50},
            {"Name":"Ali","Grade":60},
            {"Name":"Yağmur","Grade":70},
            {"Name":"Çınar","Grade":80}
           ]

df=pd.DataFrame([1,2,3,4]) 
df=pd.DataFrame(data, index=[1,2,3,4], columns=["Name","Grade"], dtype=float) #kolon isimleri sırayla Name ve Grade olur. index numaralarını da 1,2,3,4 yaptık, yani sıfırdan başlamamış olur. Gelen sayısal bilgilerin float olması gerektiğini dtype ile belirttik 
df=pd.DataFrame(dict) #sözlük veri yapısıyla DataFrame'i oluşturmak daha kolaydır
df=pd.DataFrame(dict,index=["212","232","236","456"]) #index olarak belirtilenler öğrenci numarası gibi düşünülebilir
df=pd.DataFrame(dict_list)
df=pd.DataFrame(dict_list,index=["212","232","236","456"])  #        Name  Grade
                                                            # 212   Ahmet     50
                                                            # 232     Ali     60
                                                            # 236  Yağmur     70
                                                            # 456   Çınar     80

print(df)


