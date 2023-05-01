# --- Numpy dizileri ile çalışma ---

import numpy as np

result=np.array([1,3,5,7,9])
result=np.arange(1,10) # 1 2 3 4 5 6 7 8 9 şeklinde kendisi dizi oluşturur
result=np.arange(10,100,3) #10'dan 100'e kadar 3'er 3'er
result=np.zeros(10) #10 tane sıfır
result=np.ones(10) #10 tane 1
result=np.linspace(0,100,5) #verdiğimiz aralığı 5'e bölecek
result=np.linspace(0,5,5) #[0.   1.25 2.5  3.75 5.  ]
result=np.random.randint(0,10)
result=np.random.randint(20)
result=np.random.randint(1,10,3)
result=np.random.rand(5) #float sayı üretir
result=np.random.randn(5) # -'li değerleri de katar

np_array=np.arange(50)
np_multi=np_array.reshape(5,10) #5e 10luk matris

print(np_multi.sum(axis=1)) #satırların toplamını verir
print(np_multi.sum(axis=0)) #sütunların toplam değerlerinis verir

rnd_numbers=np.random.randint(1,100,10)
print(rnd_numbers)
result=rnd_numbers.max() #üretilen sayılardan en büyüğü
result=rnd_numbers.min() #üretilen sayılardan en küçüğü
result=rnd_numbers.mean() #üretilen sayıların ortalaması
result=rnd_numbers.argmax() #en büyük sayının indeksi
result=rnd_numbers.argmin()
print(result)