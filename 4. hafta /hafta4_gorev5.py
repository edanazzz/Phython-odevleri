# Kurum: İstanbul Nişantaşı Üniversitesi
# Ders: Python ile Programlama
# Öğretim Üyesi: Dr. Öğr. Üyesi Murat Emeç
# Dönem: 2026-2027 Güz
# Öğrenci Adı Soyadı: EDA NAZ GÜLARSLAN
# Öğrenci Numarası: 20253005006
# Tarih: 18.10.2026
# Açıklama: map, filter, reduce ve partial fonksiyonları ile galaksi istatistikleri.

from functools import reduce, partial

galaksi = {
    "baglantilar": {
        "dünya": ["centauri", "sirius", "orion"],
        "centauri": ["dünya", "orion"],
        "sirius": ["dünya", "orion"],
        "orion": ["dünya", "centauri", "sirius"],
        "kara_delik": []
    }
}

# 1. Gezegen adlarının büyük harfli listesi
# Yol A: map
buyuk_harf_map = list(map(lambda x: x.upper(), galaksi["baglantilar"].keys()))
# Yol B: Liste üreteci
buyuk_harf_comp = [g.upper() for g in galaksi["baglantilar"].keys()]

# 2. En az iki bağlantısı olan gezegenler
# Yol A: filter
en_az_iki_filter = list(filter(lambda k: len(galaksi["baglantilar"][k]) >= 2, galaksi["baglantilar"]))
# Yol B: Liste üreteci
en_az_iki_comp = [k for k, v in galaksi["baglantilar"].items() if len(v) >= 2]

# 3. Toplam bağlantı sayısı
# Yol A: reduce
toplam_baglanti_reduce = reduce(lambda acc, k: acc + len(galaksi["baglantilar"][k]), galaksi["baglantilar"], 0)
# Yol B: sum
toplam_baglanti_sum = sum(len(v) for v in galaksi["baglantilar"].values())

# 4. functools.partial kullanımı
def yolculuk(mesafe, hiz):
    return mesafe / hiz

hizli_yolculuk = partial(yolculuk, hiz=3)

# Okunabilirlik Yorumu:
# Python'da liste üreteçleri (list comprehensions) ve doğrudan sum() kullanımı,
# lambda içeren map/filter/reduce yapılarına kıyasla çok daha sade, açık ve Pythonic bir yazım sunar.

print(buyuk_harf_map)
print(en_az_iki_filter)
print(toplam_baglanti_sum)
print("Hızlı yolculuk süresi (mesafe=9):", hizli_yolculuk(9))
