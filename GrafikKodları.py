import evds as e
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

evds = e.evdsAPI("APİ KEY") 

mainCategory = evds.main_categories 
subCotegory = evds.get_sub_categories(1) 
exchangeSeries = evds.get_series("bie_dkdovytl") 
bistIndexSeries = evds.get_series("bie_mkbrgn")

tcmbDollarBuyingData = evds.get_data(["TP.DK.USD.A.YTL"],startdate="01-09-2020",enddate="11-4-2024",frequency=5)
bist100Index = evds.get_data(["TP.MK.F.BILESIK"],startdate="01-09-2020",enddate="11-4-2024",frequency=5)

with pd.ExcelWriter('datalar.xlsx') as writer:
    tcmbDollarBuyingData.to_excel(writer, index=False,startrow=0,startcol=0)
    bist100Index.to_excel(writer, index=False,startrow=0,startcol=len(tcmbDollarBuyingData.columns)+1)

dataset = pd.read_excel('datalar.xlsx')

x = dataset["TP_DK_USD_A_YTL"]
y = dataset["TP_MK_F_BILESIK"]
dateXY = dataset["Tarih"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=1)
basitRegresyon = LinearRegression()
x_values = x_train.values.reshape(-1,1)
y_values = y_train.values.reshape(-1,1)
basitRegresyon.fit(x_values,y_values)

y_predicts = basitRegresyon.predict(x_test.values.reshape(-1,1))
sorted_indices = np.argsort(x_train)
x_train_sorted = x_train.values[sorted_indices]
y_train_sorted = y_train.values[sorted_indices]

#Dağılım grafiği gerçek değerlerle tahmin değerleriarasındaki ilişki
plt.scatter(y_test,y_predicts)
plt.title("Gerçek Değerler İle Tahmin Değerleri Arasındaki İlişki")  
plt.xlabel('Y-TEST DEĞERLERİ')
plt.ylabel('Y-TAHMİN DEĞERLERİ')
plt.show()

#Eğitim veri seti üzerinde yapılan regresyon analizi
plt.plot(x_train_sorted,basitRegresyon.predict(x_train_sorted.reshape(-1,1)), color='red', label ="Regresyon")
plt.scatter(x_train, y_train)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Basit Regresyon Analizi')
plt.show()

#Dolar kurunun tarihe göre artışı
plt.figure(figsize=(12,6))
plt.plot(dateXY,x)
plt.xticks(rotation=90)
plt.title("TCMB Dolar Alış Kuru 2020-2024")
plt.xlabel("Tarih")
plt.ylabel("Dolar Kuru")
plt.show()

#Borsa 100 Endeksinin Tarihe göre artışı
plt.figure(figsize=(12,6))
plt.plot(dateXY,y)
plt.xticks(rotation=90)
plt.title("Borsa 100 Endeksi(XU100) 2020-2024")
plt.xlabel("Tarih")
plt.ylabel("Borsa 100 Endeksi(XU100)")
plt.show()

#Borsa 100 Endeksi ve Dolar Kurunun birbirine etkisi
plt.figure(figsize=(12,6))
plt.plot(x,y)
plt.title("Borsa 100 Endeksi ile Dolar Arasındaki İlişki")
plt.xlabel("TCMB Dolar Alış Kuru")
plt.ylabel("Borsa 100 Endeksi")
plt.show()


b0 = basitRegresyon.intercept_ #Regresyon modelinin kesme noktasını temsil eder β0 KATSAYISI
b1 = basitRegresyon.coef_ #Regresyon modelinin katsayısını temsil eder β (beta) KATSAYILARI
print("Kurulan Regresyon Modeli: Y = {} + {}*x".format(basitRegresyon.intercept_[0].round(2),basitRegresyon.coef_[0][0].round(2)))


#Eğitim veri setindeki bağımsız değişkenlerin bağımlı değişkenı açıklama başarısını ölçen r kare değeri
#Ortalama mutlak hata = Tahminin gerçek değere olan mutlak farkını alır
#Ortalama hata karesi = Tahminin gerçek değere olan farkının karesini alır
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
y_predict_train = basitRegresyon.predict(x_values)

print(r2_score(y_train,y_predict_train).round(2))
print(mean_squared_error(y_train,y_predict_train).round(2))
print(mean_absolute_error(y_train,y_predict_train).round(2))