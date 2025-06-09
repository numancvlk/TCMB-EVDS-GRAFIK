# Borsa 100 Endeksi ve Dolar Kuru Arasındaki İlişki: Veri Analizi ve Regresyon Modeli
## Proje Özeti
Bu proje, Türk Lirası (TRY) ile Amerikan Doları (USD) arasındaki döviz kuru ile Borsa İstanbul 100 Endeksi (BIST 100) arasındaki ilişkiyi inceleyen basit bir doğrusal regresyon analizi gerçekleştirir. Veri, Türkiye Cumhuriyet Merkez Bankası (TCMB) ve İstanbul Borsası'ndan alınmaktadır. Amaç, bu iki değişken arasındaki ilişkiyi keşfetmek ve birini diğerine göre tahmin edebilecek bir regresyon modeli oluşturmaktır.

## Veri Kaynakları
TCMB Dolar Alış Kuru: USD/TRY döviz kuru verisi.

Borsa 100 Endeksi (BIST 100): Borsa İstanbul 100 Endeksi (XU100) verisi.

Veri, Türkiye İstatistik Kurumu (EVDS) üzerinden evdsAPI kullanılarak alınmakta ve işlenmesi için bir Excel dosyasına kaydedilmektedir.

## Temel Adımlar
Veri Toplama: TCMB'nin dolar alış kuru ve Borsa İstanbul 100 Endeksi verileri alınır.

Veri İşleme: Veriler Excel dosyasına kaydedilir ve pandas ile işlenir.

Eğitim ve Test Verisi Ayırma: Veriler, eğitim ve test veri setlerine ayrılır.

Regresyon Modeli Kurma: Basit doğrusal regresyon modeli oluşturulur.

Model Değerlendirmesi: Modelin doğruluğu, R-kare, ortalama mutlak hata ve ortalama hata kareleri gibi metriklerle değerlendirilir.

Görselleştirme: Regresyon analizi ve veri ilişkileri görselleştirilir.

## Kullanılan Kütüphaneler
evds: EVDS API'si üzerinden veri çekmek için kullanılır.

pandas: Veriyi işlemek için kullanılır.

numpy: Veri manipülasyonu için kullanılır.

matplotlib: Veri görselleştirmesi için kullanılır.

sklearn: Doğrusal regresyon modeli oluşturmak ve değerlendirmek için kullanılır.

## Uygulama Adımları
Veri Çekme: TCMB dolar alış kuru ve BIST 100 endeksi verileri API üzerinden çekilir.

Veri Kaydetme: Veriler bir Excel dosyasına kaydedilir.

Model Kurma: Verilerle basit doğrusal regresyon modeli oluşturulur.

Grafikler: Gerçek ve tahmin edilen değerler arasındaki ilişki, eğitim verisi üzerindeki regresyon analizi ve iki değişkenin zaman içindeki artışı görselleştirilir.

## Model Sonuçları
Modelin doğruluğu, aşağıdaki metriklerle değerlendirilmiştir:

R-Kare (R²): Modelin veriye uyumunu gösterir.

Ortalama Mutlak Hata (MAE): Tahmin edilen değerlerin gerçek değerlerle ne kadar uyumlu olduğunu ölçer.

Ortalama Kare Hatası (MSE): Tahmin edilen değerlerin gerçek değerlerle olan farklarının karesinin ortalamasıdır.

## Kurulum
Bu projeyi çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

Gerekli Python kütüphanelerini yükleyin:

bash
Copy
pip install evds pandas numpy matplotlib scikit-learn
evdsAPI anahtarınızı alarak yerine yazın.

Projeyi çalıştırarak veriyi çekebilir, regresyon analizi yapabilir ve görselleştirmeleri görebilirsiniz.

## Çıktılar
Regresyon Modeli: Basit doğrusal regresyon modelinin doğruluğu ve formülü.

Grafikler: Gerçek ve tahmin edilen değerler arasındaki ilişki, BIST 100 Endeksi ve Dolar kuru arasındaki ilişki, zaman serisi grafikleri vb.

## İletişim
Herhangi bir soru ya da öneriniz olursa, lütfen iletişime geçin.

### Bu proje, sadece portföy amacıyla ve ticari bir amaç gütmeden paylaşılmaktadır.
### This project is shared solely for portfolio purposes and without any commercial intent.
