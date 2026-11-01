# Ad Soyad: Eda Naz Gülarslan
# Numara: 20253005006
# Tarih: 01.11.2026
# Açıklama: Girilen metnin harf, sesli, sessiz, rakam ve kelime sayılarını bulur; palindrom kontrolü yapar.

cumle = input("Cümle: ")

harf_sayisi = 0
sesli_sayisi = 0
sessiz_sayisi = 0
rakam_sayisi = 0
kelime_sayisi = 0

ters_cumle = ""
sadece_harfler = ""
sesliler = "aeıioöuüAEIİOÖUÜ"

onceki_karakter_bosluk = True  # Kelime saymak için bayrak (flag) değişkeni

for karakter in cumle:
    # Tersini oluşturma
    ters_cumle = karakter + ters_cumle

    # Harf ve Rakam ayrımı
    if karakter.isalpha():
        harf_sayisi += 1
        kucuk_harf = karakter.lower()
        sadece_harfler += kucuk_harf
        
        if karakter in sesliler:
            sesli_sayisi += 1
        else:
            sessiz_sayisi += 1
            
    elif karakter.isdigit():
        rakam_sayisi += 1

    # Kelime sayma mantığı (Bayrak kullanımı)
    if karakter == " " or karakter == "\t":
        onceki_karakter_bosluk = True
    else:
        if onceki_karakter_bosluk:
            kelime_sayisi += 1
            onceki_karakter_bosluk = False

# Palindrom kontrolü (Sadece harflerin tersini manuel bularak)
ters_harfler = ""
for h in sadece_harfler:
    ters_harfler = h + ters_harfler

if sadece_harfler == ters_harfler and len(sadece_harfler) > 0:
    palindrom_durumu = "Palindrom"
else:
    palindrom_durumu = "Palindrom değil"

print(f"Harf: {harf_sayisi} Sesli: {sesli_sayisi} Sessiz: {sessiz_sayisi} Rakam: {rakam_sayisi} Kelime: {kelime_sayisi}")
print(f"Ters: {ters_cumle}")
print(palindrom_durumu)
