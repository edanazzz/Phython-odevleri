# Kurum: İstanbul Nişantaşı Üniversitesi
# Ders: Python ile Programlama
# Öğretim Üyesi: Dr. Öğr. Üyesi Murat Emeç
# Dönem: 2026-2027 Güz
# Öğrenci Adı Soyadı: Eda Naz Gülarslan
# Öğrenci Numarası: 20253005006
# Tarih: 04.10.2026
# Açıklama: 0 ile 999 arasındaki bir tam sayının basamaklarındaki rakamları toplar.

sayi = int(input("Sayı (0-999): "))

birler = sayi % 10
kalan = sayi // 10

onlar = kalan % 10
yuzler = kalan // 10

toplam = birler + onlar + yuzler

print(f"Rakamlar toplamı: {toplam}")
