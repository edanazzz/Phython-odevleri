# Kurum: İstanbul Nişantaşı Üniversitesi
# Ders: Python ile Programlama
# Öğretim Üyesi: Dr. Öğr. Üyesi Murat Emeç
# Dönem: 2026-2027 Güz
# Öğrenci Adı Soyadı: EDA NAZ GÜLARSLAN
# Öğrenci Numarası: 20253005006
# Tarih: 18.10.2026
# Açıklama: zamanlayici() üreteci ile meşgul bekleme (busy waiting) ve sleep farkı.

import time

def zamanlayici(aralik: float):
    """Her aralık saniyede bir tetiklenen üreteç."""
    son_zaman = time.perf_counter()
    while True:
        simdi = time.perf_counter()
        if simdi - son_zaman >= aralik:
            son_zaman = simdi
            yield True
        else:
            yield False

# 10 saniye boyunca çalıştırma:
baslangic = time.perf_counter()
zamanlayici_2 = zamanlayici(2.0)
zamanlayici_5 = zamanlayici(5.0)

while time.perf_counter() - baslangic < 10.0:
    if next(zamanlayici_2):
        print("tik")
    if next(zamanlayici_5):
        print("tak")

"""
AÇIKLAMA:
Neden 'meşgul bekleme' (busy waiting)?
Döngü sürekli koşul kontrolü yaparak işlemciyi (CPU) %100 meşgul tutar; işlemci boşta durmak
yerine sürekli aradaki zaman farkını kontrol eder.

time.sleep() ile farkı:
time.sleep() işletim sistemine o iş parçacığını (thread) belirtilen süre boyunca askıya alma
komutu verir. Böylece işlemci gereksiz döngülerle yorulmaz ve başka görevleri işleyebilir.
"""
