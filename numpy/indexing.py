# --- Numpy dizilerinin indekslenmesi ---

import numpy as np

numbers=np.array([0,5,10,15,20,25,50,75])
result=numbers[5]
result=numbers[0:3] #numbers dizisinde 0'dan başlayarak 3. indekse kadar alır
result=numbers[::-1] #liste ters çevrilir

numbers2=np.array([[0,5,10],[15,20,25],[50,75,85]])
result=numbers2[0] # [ 0  5 10]
result=numbers2[2,1] #75
result=numbers2[:,2] #bütün satırlar arasından 2.indekstekileri alır [10,25,85]
result=numbers2[:,0:2]  #  [[ 0  5]
                        #  [15 20]
                        #  [50 75]]
result=numbers2[-1,:] #son kolondaki elemanları alır [50 75 85]
result=numbers2[:2,:2]  #[[ 0  5]
                        #[15 20]]

print(result)

arr1=np.arange(0,10)
arr2=arr1 #referans kopyalaması yapılmış olur yani hem arr2 hem de arr1 aynı adresi göstermiş olur
#arr2=arr1.copy() #arr1'in kopyası çıkarılıp arr2'ye atıldığından dolayı farklı adresleri gösterecekler

arr2[0]=20

print(arr1) #diziler referans tipler olduğu için kopyalama işleminde birbirine adresleri aktarılır bu yüzden de herhangi birinde elemanı değiştirdiğimizde diğerine de yansımış olur
print(arr2)