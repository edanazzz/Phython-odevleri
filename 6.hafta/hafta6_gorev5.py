# Ad Soyad: Eda Naz Gülarslan
# Numara: 20253005006
# Tarih: 01.11.2026
# Açıklama: continue, break ve while-else döngü kontrol yapılarını kullanan adam asmaca oyunu.

gizli_kelime = "KOŞUL"
denenenler = ""
hata_sayisi = 0
maks_hata = 6

while hata_sayisi < maks_hata:
    # Ekranda gösterilecek metni oluştur
    gorunum = ""
    tum_harfler_bulundu = True
    
    for harf in gizli_kelime:
        if harf in denenenler:
            gorunum += harf + " "
        else:
            gorunum += "_ "
            tum_harfler_bulundu = False

    # Kazanma Durumu (break kullanımı)
    if tum_harfler_bulundu:
        print(gorunum.strip() + "    Kazandınız!")
        break

    print(gorunum.strip() + f"    (hata: {hata_sayisi}/{maks_hata})")
    giris = input("Harf: ")

    # Hatalı veya fazla karakter girişini atlama (continue kullanımı)
    if len(giris) != 1 or not giris.isalpha():
        continue

    # İpucu: Türkçe karakter sorununu manuel çözüyoruz
    if giris == 'i':
        tahmin = 'İ'
    elif giris == 'ı':
        tahmin = 'I'
    else:
        tahmin = giris.upper()

    # Daha önce girilmiş harfi atlama (continue kullanımı)
    if tahmin in denenenler:
        print("Bu harfi zaten denediniz.")
        continue

    denenenler += tahmin

    if tahmin not in gizli_kelime:
        hata_sayisi += 1

# Döngü break ile kırılmadan biterse çalışır (while...else kullanımı)
else:
    print(f"(hata: {hata_sayisi}/{maks_hata})")
    print(f"Kaybettiniz! Gizli kelime: {gizli_kelime}")
