 # --- Pandas ile Join ve Merge ---

import pandas as pd


# --- MERGE İŞLEMİ ---

customers={
    "CustomerId":[1,2,3,4],
    "FirstName":["Ahmet","Ali","Hasan","Canan"],
    "LastName":["Yılmaz","Korkmaz","Çelik","Toprak"]
}

orders={
    "OrderId": [10,11,12,13],
    "CustomerId":[1,2,5,7],
    "OrderDate":["2010-07-04","2010-08-04","2010-07-07","2012-07-05"]
}

# Yukarıdaki dict yapısını DataFrame'e çevirelim

df_customers=pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
df_orders=pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])


print(df_customers)
print(df_orders)

result=pd.merge(df_customers,df_orders,how="inner") # innerjoin işlemiyle iki tabloyu birleştirmiş olduk. Sadece siparişi olan kayıtlar gelmiş olur.
result=pd.merge(df_customers,df_orders,how="left") # tüm müşteri bilgileri gelir. Siparişi olmayan kullanıcılar için de NaN değeri yazar.
result=pd.merge(df_customers,df_orders,how="right") # tüm sipariş bilgileri gelir fakat siparişi verenin adı yoksa NaN yazacak.
result=pd.merge(df_customers,df_orders,how="outer") # sağ ve soldaki bütün kayıtlar getirilir.

# print(result)



# --- İki ayrı tabloyu concat ile birleştirme

customersA={
    "CustomerId":[1,2,3,4],
    "FirstName":["Ahmet","Ali","Hasan","Canan"],
    "LastName":["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB={
    "CustomerId":[4,5,6,7],
    "FirstName":["Yağmur","Çınar","Cengiz","Can"],
    "LastName":["Bilge","Turan","Yılmaz","Turan"]
}

df_customersA=pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
df_customersB=pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])

result=pd.concat([df_customersA,df_customersB])

print(result)