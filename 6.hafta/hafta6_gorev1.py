# Ad Soyad: Eda Naz Gülarslan
# Numara: 20253005006
# Tarih: 01.11.2026
# Açıklama: Kenar uzunluklarına göre üçgenin türünü, çevresini, alanını ve en büyük açısını hesaplar.

import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# 1. Girdi Doğrulama (Üçgen Eşitsizliği ve Pozitiflik)
if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Hata: Kenarlar pozitif olmalı ve üçgen eşitsizliğini sağlamalıdır.")
else:
    # 2. İşlem
    # Liste kullanılamayacağı için en uzun kenarı if ile buluyoruz
    if a >= b and a >= c:
        en_uzun, kenar1, kenar2 = a, b, c
    elif b >= a and b >= c:
        en_uzun, kenar1, kenar2 = b, a, c
    else:
        en_uzun, kenar1, kenar2 = c, a, b

    # Kenarlarına göre tür
    if a == b == c:
        kenar_turu = "Eşkenar"
    elif a == b or a == c or b == c:
        kenar_turu = "İkizkenar"
    else:
        kenar_turu = "Çeşitkenar"

    # Açı hesaplama (Radyan'dan Dereceye)
    cos_alfa = (kenar1**2 + kenar2**2 - en_uzun**2) / (2 * kenar1 * kenar2)
    radyan = math.acos(cos_alfa)
    aci = math.degrees(radyan)

    # Açısına göre tür
    if math.isclose(aci, 90.0):
        aci_turu = "Dik açılı"
    elif aci > 90.0:
        aci_turu = "Geniş açılı"
    else:
        aci_turu = "Dar açılı"

    # Çevre ve Alan (Heron Formülü)
    cevre = a + b + c
    u = cevre / 2
    alan = math.sqrt(u * (u - a) * (u - b) * (u - c))

    # 3. Çıktı
    print(f"Tür: {kenar_turu}, {aci_turu}")
    print(f"Çevre: {cevre:.2f} Alan: {alan:.2f} En büyük açı: {aci:.2f}°")
