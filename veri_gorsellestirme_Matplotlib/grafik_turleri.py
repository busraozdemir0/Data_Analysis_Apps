import matplotlib.pyplot as plt

# *** Bazı oyuncuların yıllara göre attığı gol senaryosuna göre grafik
# 1- Stack Plot

"""
yil=[2011,2012,2013,2014,2015]

oyuncu1=[8,10,12,7,9]
oyuncu2=[7,12,5,15,21]
oyuncu3=[18,20,22,25,19]

plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors=["y","r","b"])
plt.title("Yıllara göre atılan goller")
plt.xlabel("Yıl")
plt.ylabel("Gol Sayısı")
plt.legend()
plt.show()
"""

# 2- Pie (Pasta) Grafiği
"""
goal_types="Penaltı","Kaleye Atılan Şut"," Serbest Vuruş" # pasta grafiğinin etrafında olacak bilgiler

goals=[12,35,7]
clrs=["y","r","b"] # renkler

plt.pie(goals,labels=goal_types,colors=clrs,shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%") # explode=(0.05,0.05,0.05) ile pasta grafiklerinin her bir parçası arasında 0.05'lik mesafe olmasını sağladık.
                                                                                                    # autopct="%1.1f%%" => pasta grafikleri üzerinde yüzdelik değeri gelmesi için yüzdelik formatı belirttik.
plt.show()

"""

# 3- Bar Grafiği
"""
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5) # width=.5 => bar'ın genişliğini belirttik
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5)
# renk belirtmezsek varsayılan renkler gelir (turuncu, mavi)
plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe (km)")
plt.title("Araç Bilgileri")

plt.show()

"""

# 4- Histogram Grafiği
# *** Belli yaş grupları arasındaki insanların sayısını verir

yaslar=[22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
yas_gruplari=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plt.xlabel("Yaş Grupları")
plt.xlabel("Kişi Sayısı")
plt.title("Histogram Grafiği")

plt.show()