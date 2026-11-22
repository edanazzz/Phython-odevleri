# Ad Soyad: Eda Naz Gülarslan
# Numara: 20253005006
# Tarih: 22.11.2026
# Açıklama: Onluk tabandan 2-16 arası tabanlara ve tersine (Horner yöntemiyle) dönüşüm yapan program.

RAKAM = "0123456789ABCDEF"


def onluktan(n, taban):
    """Onluk tabandaki n sayısını 2-16 arası verilen tabana çevirip metin döndürür."""
    if n == 0:
        return "0"

    sonuc = ""
    while n > 0:
        kalan = n % taban
        sonuc = RAKAM[kalan] + sonuc
        n //= taban
    return sonuc


def onluga(metin, taban):
    """Verilen tabandaki metni Horner yöntemiyle onluk tabana çevirir."""
    metin = metin.strip().upper()
    sonuc = 0
    for ch in metin:
        basamak = RAKAM.find(ch)
        sonuc = sonuc * taban + basamak
    return sonuc


# Örnek testler ve hazır fonksiyonlarla doğrulama
print("2026 ikilik:", onluktan(2026, 2), "| Kontrol:", bin(2026)[2:])
print("2026 sekizlik:", onluktan(2026, 8), "| Kontrol:", oct(2026)[2:])
print("2026 onaltılık:", onluktan(2026, 16), "| Kontrol:", hex(2026)[2:].upper())

print("7ea (16) ->", onluga("7ea", 16), "| Kontrol:", int("7ea", 16))
print("11111101010 (2) ->", onluga("11111101010", 2), "| Kontrol:", int("11111101010", 2))
print("3752 (8) ->", onluga("3752", 8), "| Kontrol:", int("3752", 8))

# Ek farklı testler
print("0 ikilik:", onluktan(0, 2))
print("255 onaltılık:", onluktan(255, 16), "| Geri dönüşüm:", onluga("ff", 16))
