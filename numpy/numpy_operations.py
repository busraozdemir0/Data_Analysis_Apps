# --- Numpy dizi operasyonları ---

import numpy as np

numbers1=np.random.randint(10,100,6)
numbers2=np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result=numbers1+numbers2 #oluşturulan iki rastgele diziyi toplar
result=numbers1+10 #1 numaralı dizideki her bir elemana 10 sayısı eklenir

result=numbers1-numbers2
result=numbers2*10
result=numbers1/numbers2

result=np.sin(numbers1)
result=np.cos(numbers1)
result=np.sqrt(numbers1) #numbers1'ideki her bir elemanın karekökünü alır
result=np.log(numbers1)

mnumbers1=numbers1.reshape(2,3)
mnumbers2=numbers2.reshape(2,3)

# print(mnumbers1)
# print(mnumbers2)

result=np.vstack((mnumbers1,mnumbers2)) #dikey olarak matrisleri birleştirme işlemi yapar
result=np.hstack((mnumbers1,mnumbers2)) #yatay olarak matrisleri birleştirme işlemi yapar

result=numbers1 >= 5 #numbers1'deki elemanları tek tek gezer ve 5'ten büyük olup olmadığını kontrol ederek bool bir değer döndürür
result=numbers1 % 2 == 0 #çift sayılarda true değeri döndürür

print(numbers1[result]) #koşulu sağlayan elemanları da dizi şeklinde yazdırır

print(result)