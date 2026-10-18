# Kurum: İstanbul Nişantaşı Üniversitesi
# Ders: Python ile Programlama
# Öğretim Üyesi: Dr. Öğr. Üyesi Murat Emeç
# Dönem: 2026-2027 Güz
# Öğrenci Adı Soyadı: EDA NAZ GÜLARSLAN
# Öğrenci Numarası: 20253005006
# Tarih: 18.10.2026
# Açıklama: lru_cache ile önbellekli rota sayacı ve süre karşılaştırması.

import time
from functools import lru_cache

# Mars'sız varsayılan galaksi bağlantı verisi
galaksi = {
    "baglantilar": {
        "dünya": ["centauri", "sirius", "orion"],
        "centauri": ["dünya", "orion"],
        "sirius": ["dünya", "orion"],
        "orion": ["dünya", "centauri", "sirius"],
        "kara_delik": []
    }
}

def rota_sayaci(baglantilar):
    """İçinde @lru_cache ile önbelleklenmiş rota_sayisi fonksiyonunu döndürür."""
    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen, adim):
        if adim == 0:
            return 1
        toplam = 0
        for komsu in baglantilar.get(gezegen, []):
            toplam += rota_sayisi(komsu, adim - 1)
        return toplam

    return rota_sayisi

# --- Önbelleksiz Fonksiyon (Karşılaştırma için) ---
def rota_sayisi_onbelleksiz(baglantilar, gezegen, adim):
    if adim == 0:
        return 1
    toplam = 0
    for komsu in baglantilar.get(gezegen, []):
        toplam += rota_sayisi_onbelleksiz(baglantilar, komsu, adim - 1)
    return toplam

# Testler:
say = rota_sayaci(galaksi["baglantilar"])
print("Test Değerleri:", (say("dünya", 3), say("dünya", 10), say("dünya", 40)))

# Süre Ölçümü (adim = 20):
t1 = time.perf_counter()
sonuc_onbelleksiz = rota_sayisi_onbelleksiz(galaksi["baglantilar"], "dünya", 20)
t2 = time.perf_counter()
sure_onbelleksiz = t2 - t1

say_yeni = rota_sayaci(galaksi["baglantilar"])
t3 = time.perf_counter()
sonuc_onbellekli = say_yeni("dünya", 20)
t4 = time.perf_counter()
sure_onbellekli = t4 - t3

print(f"Önbelleksiz süre (adim=20): {sure_onbelleksiz:.6f} saniye")
print(f"Önbellekli süre (adim=20)  : {sure_onbellekli:.6f} saniye")
print("Cache Bilgisi:", say_yeni.__closure__[0].cell_contents.cache_info() if hasattr(say_yeni, '__closure__') else "lru_cache aktif")
