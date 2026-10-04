# Kurum: İstanbul Nişantaşı Üniversitesi
# Ders: Python ile Programlama
# Öğretim Üyesi: Dr. Öğr. Üyesi Murat Emeç
# Dönem: 2026-2027 Güz
# Öğrenci Adı Soyadı: Eda Naz Gülarslan
# Öğrenci Numarası: 20253005006
# Tarih: 04.10.2026
# Açıklama: Yarıçap ve yükseklik ile silindirin taban alanını ve hacmini hesaplar.

PI = 3.14159

yaricap = float(input("Yarıçap: "))
yukseklik = float(input("Yükseklik: "))

taban_alani = PI * (yaricap ** 2)
hacim = taban_alani * yukseklik

print(f"Taban alanı: {taban_alani}")
print(f"Hacim: {hacim}")
