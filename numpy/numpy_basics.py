# büyük verilerle çalışmak için birebir
# dosya adı numpy olursa yani kütüphane adıyla aynı olursa hata verecektir.
""" Python’da dizilerin amacına hizmet eden listelerimiz var, ancak işlenmesi yavaştır. 
NumPy, geleneksel Python listelerinden 50 kata kadar daha hızlı bir dizi nesnesi sağlamayı amaçlamaktadır. 
NumPy’deki dizi nesnesi (array) ndarray olarak adlandırılır ve ndarray, 
çalışmayı çok kolaylaştıran birçok destekleyici işlev sağlar. Diziler, hız ve kaynakların 
çok önemli olduğu veri biliminde çok sık kullanılır.
"""

import numpy as np

# python list
py_list=[1,2,3,4,5,6,7,8,9]

# numpy array
np_array=np.array([1,2,3,4,5,6,7,8,9]) #listeyi diziye çevirir

print(type(py_list))
print(type(np_array))

py_multi=[[1,2,3],[4,5,6],[7,8,9]]
np_multi=np_array.reshape(3,3) #3 satır ve 3 sütundan oluşan matris

print(py_multi)
print(np_multi)