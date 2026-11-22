# Ad Soyad: Eda Naz Gülarslan
# Numara: 20253005006
# Tarih: 22.11.2026
# Açıklama: Onluk sayıları Roma rakamına ve Roma rakamlarını onluk sayıya çeviren program.

def onluktan_romaya(n):
    """Pozitif tam sayıyı liste/sözlük kullanmadan Roma rakamına çevirir."""
    sonuc = ""

    while n >= 1000:
        sonuc += "M"
        n -= 1000
    while n >= 900:
        sonuc += "CM"
        n -= 900
    while n >= 500:
        sonuc += "D"
        n -= 500
    while n >= 400:
        sonuc += "CD"
        n -= 400
    while n >= 100:
        sonuc += "C"
        n -= 100
    while n >= 90:
        sonuc += "XC"
        n -= 90
    while n >= 50:
        sonuc += "L"
        n -= 50
    while n >= 40:
        sonuc += "XL"
        n -= 40
    while n >= 10:
        sonuc += "X"
        n -= 10
    while n >= 9:
        sonuc += "IX"
        n -= 9
    while n >= 5:
        sonuc += "V"
        n -= 5
    while n >= 4:
        sonuc += "IV"
        n -= 4
    while n >= 1:
        sonuc += "I"
        n -= 1

    return sonuc


def roma_harf_degeri(ch):
    """Tek bir Roma rakamı harfinin sayısal karşılığını döndürür."""
    if ch == "M":
        return 1000
    elif ch == "D":
        return 500
    elif ch == "C":
        return 100
    elif ch == "L":
        return 50
    elif ch == "X":
        return 10
    elif ch == "V":
        return 5
    elif ch == "I":
        return 1
    return 0


def romadan_onluga(metin):
    """Roma rakamı metnini onluk tam sayıya çevirir."""
    metin = metin.strip().upper()
    toplam = 0
    uzunluk = len(metin)

    for i in range(uzunluk):
        su_an = roma_harf_degeri(metin[i])
        if i + 1 < uzunluk and su_an < roma_harf_degeri(metin[i + 1]):
            toplam -= su_an
        else:
            toplam += su_an

    return toplam


# Örnek testler
print("2026 ->", onluktan_romaya(2026))         # MMXXVI
print("1994 ->", onluktan_romaya(1994))         # MCMXCIV
print("XLII ->", romadan_onluga("XLII"))        # 42

# Ek farklı testler
print("58 ->", onluktan_romaya(58))             # LVIII
print("MCMXCIV ->", romadan_onluga("MCMXCIV"))  # 1994
print("mmxxvi ->", romadan_onluga("mmxxvi"))    # 2026
