# Ad Soyad: Eda Naz Gülarslan
# Numara: 20253005006
# Tarih: 01.11.2026
# Açıklama: Collatz dizisi kurallarını ternary operatör ile uygulayarak uzunluk ve maksimum zincir tespiti yapar.

n = int(input("n: "))

# A Şıkkı: Tek bir sayı için hesaplama
adim = 0
en_yuksek = n
gecici_n = n

while gecici_n != 1:
    # HOCANIN İSTEDİĞİ TEK SATIRLIK KOŞUL (Ternary Operator)
    gecici_n = gecici_n // 2 if gecici_n % 2 == 0 else 3 * gecici_n + 1
    
    adim += 1
    if gecici_n > en_yuksek:
        en_yuksek = gecici_n
        
print(f"{n} -> 1: {adim} adım, en yüksek değer {en_yuksek}")

# B Şıkkı: Belirli bir üst sınıra kadar en uzun zinciri bulma
ust_sinir = int(input("Üst sınır: "))
en_uzun_zincir_baslangici = 1
maks_adim = 0

for baslangic in range(1, ust_sinir + 1):
    guncel_sayi = baslangic
    mevcut_adim = 0
    
    while guncel_sayi != 1:
        # HOCANIN İSTEDİĞİ TEK SATIRLIK KOŞUL
        guncel_sayi = guncel_sayi // 2 if guncel_sayi % 2 == 0 else 3 * guncel_sayi + 1
        mevcut_adim += 1

    if mevcut_adim > maks_adim:
        maks_adim = mevcut_adim
        en_uzun_zincir_baslangici = baslangic

print(f"1-{ust_sinir} arasında en uzun zincir: {en_uzun_zincir_baslangici} ({maks_adim} adım)")
