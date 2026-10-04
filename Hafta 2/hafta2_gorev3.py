# Kurum: İstanbul Nişantaşı Üniversitesi
# Ders: Python ile Programlama
# Öğretim Üyesi: Dr. Öğr. Üyesi Murat Emeç
# Dönem: 2026-2027 Güz
# Öğrenci Adı Soyadı: Eda Naz Gülarslan
# Öğrenci Numarası: 20253005006
# Tarih: 04.10.2026
# Açıklama: Girilen toplam saniyeyi gün, saat, dakika ve saniyeye ayrıştırır.

toplam_saniye = int(input("Saniye: "))

# Bir gündeki toplam saniye: 24 * 3600 = 86400
gun = toplam_saniye // 86400
kalan = toplam_saniye % 86400

# Bir saatteki toplam saniye: 3600
saat = kalan // 3600
kalan = kalan % 3600

# Bir dakikadaki toplam saniye: 60
dakika = kalan // 60
saniye = kalan % 60

print(f"{toplam_saniye} saniye = {gun} gün {saat} saat {dakika} dakika {saniye} saniye")
