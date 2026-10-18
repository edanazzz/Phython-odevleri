# Kurum: İstanbul Nişantaşı Üniversitesi
# Ders: Python ile Programlama
# Öğretim Üyesi: Dr. Öğr. Üyesi Murat Emeç
# Dönem: 2026-2027 Güz
# Öğrenci Adı Soyadı: EDA NAZ GÜLARSLAN
# Öğrenci Numarası: 20253005006
# Tarih: 18.10.2026
# Açıklama: Yakıt göstergesi üreteci ve travel() döngüsü simülasyonu.

def yakit_gostergesi(yakit: int, tuketim: int):
    """
    Her next() çağrısında yakıtı tüketim kadar azaltıp kalan yakıtı üretir.
    Yakıt 0'a inince durur.
    """
    kalan_yakit = yakit
    while kalan_yakit > 0:
        kalan_yakit -= tuketim
        if kalan_yakit < 0:
            kalan_yakit = 0
        yield kalan_yakit
        if kalan_yakit == 0:
            break

# Örnek test çağrısı
print(list(yakit_gostergesi(100, 30)))

def travel(baslangic_yakit: int = 100, tuketim: int = 5):
    """Her yolculukta yakıt çeker; yakıt bitince oyunu kaybettirir."""
    gosterge = yakit_gostergesi(baslangic_yakit, tuketim)
    try:
        while True:
            mevcut_yakit = next(gosterge)
            # Her yolculuk adımı simülasyonu
    except StopIteration:
        print("Yakıtın bitti, uzayda sürükleniyorsun...")

# travel() fonksiyonunu test etmek için:
travel(15, 5)
