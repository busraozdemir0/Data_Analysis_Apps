# Matplodlib kütüphanesi ile verileri grafiklere gökerek görselleştirme işlemi yapabiliriz.

import matplotlib.pyplot as plt
import numpy as np

"""
x=[1,2,3,4]
y=[1,4,9,16]

#plt.plot(x,y,color="red",linewidth="5") # x ve y listesindeki verileri göndererek grafik oluşmasını sağladık.
                                        # color ile çizgi renginin kırmızı olmasını belirttik, linewidth ile çizgi kalınlığını belirttik.
# plt.plot(x,y,"--g") # "--g"=> düz çizgi değil de kesikli çizgi halinde gelmesi için
plt.plot(x,y,"o--r")  # kırmızı kesikli çizgi ve çizgi üzerinde daire şeklinde işaretçiler                                  
plt.axis([0,6,0,20]) # axis içerisinde liste gönderebiliyoruz. 0,6 x eksenini; 0,20 de y eksenini belirtir.

plt.title("Grafik Başlığı") # grafiğe başlık vermek için
plt.xlabel("x label") # x ekseni için başlık
plt.ylabel("y label") # y ekseni için başlık

plt.show() # diyagramı göstermek için

"""
# --- örnek grafik oluşturma ---

"""
x=np.linspace(0,2,100)

plt.plot(x,x, label="linear",color="red")
plt.plot(x,x**2, label="quadratic",color="yellow")
plt.plot(x,x**3, label="cubic",color="green")

plt.xlabel("x label")
plt.ylabel("y label")

plt.title("simple plot")

plt.legend() # label'da verilen değerlerin ekranda gösterilmesi için

plt.show() # diyagramı göstermek için

"""
# --- alt alta 3 grafik oluşturma ---

"""
x=np.linspace(0,2,100)

fig,axs=plt.subplots(3) # 3 tane axes alanı oluşturduk. Aynı karede üç tane grafik gösterebilmek için

axs[0].plot(x,x, color="red")
axs[0].set_title("linear")

axs[1].plot(x,x**2, color="yellow")
axs[0].set_title("quadratic")

axs[2].plot(x,x**3, color="green") # bu şekilde alt alta 3 tane grafik oluşturulmuş olduk
axs[0].set_title("cubic")

plt.tight_layout() # başlıklar birbirine girmemesi için layout türünü değiştirdik.

"""
# --- aynı düzlem üzerinde 4 grafik oluşturma ---

"""
x=np.linspace(0,2,100)

fig,axs=plt.subplots(2,2) # figürü ikiye ikilik şekilde ayırdık. Bu şekilde her bir axes'in konumunu belirterek grafik ekleyebiliriz.
fig.suptitle("Grafik Başlığı")

axs[0,0].plot(x,x, color="red") 
axs[0,1].plot(x,x**2, color="yellow")
axs[1,0].plot(x,x**3, color="green")
axs[1,1].plot(x,x**4, color="blue") # her biri için x,y düzlemindeki konumunu belirterek (1,1 => en alt ve sağda yer alacak olan grafik) bir sayfada 4 grafik oluşturuldu.

plt.show()
"""

# --- nba.csv dosyasındaki verilere  göre grafik oluşturma --- 

import pandas as pd

df=pd.read_csv("pandas/datasets/nba.csv")

df=df.drop(["Number"],axis=1).groupby("Team").mean() # Number kolonunu sildikten sonra Team takımına göre gruplayıp ortalamalarını aldık

df.head(5).plot(subplots=True) # nba'daki ilk 5 oyuncuların sayısal kolonlarının ortalamasını grafikte gösteriyoruz
plt.legend()

plt.show()