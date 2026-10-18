# Kurum: İstanbul Nişantaşı Üniversitesi
# Ders: Python ile Programlama
# Öğretim Üyesi: Dr. Öğr. Üyesi Murat Emeç
# Dönem: 2026-2027 Güz
# Öğrenci Adı Soyadı: EDA NAZ GÜLARSLAN
# Öğrenci Numarası: 20253005006
# Tarih: 18.10.2026
# Açıklama: Sonsuz Fibonacci üreteci; next(), islice ve takewhile ile test edilmesi.

import itertools

def fibonacci():
    """Sonsuz Fibonacci serisi üreten üreteç (generator)."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# --- 1. next() ile ilk üç değeri alma ---
g = fibonacci()
print("next(g) ile ilk 3 değer:", (next(g), next(g), next(g)))

# --- 2. itertools.islice ile ilk 12 değeri alma ---
print("islice ile ilk 12 değer:", list(itertools.islice(fibonacci(), 12)))

# --- 3. itertools.takewhile ile 100'den küçük değerleri alma ---
print("takewhile (< 100):", list(itertools.takewhile(lambda x: x < 100, fibonacci())))

# --- 4. Üretecin tek kullanımlık olduğunu gösterme ---
uretec = fibonacci()
ilk_cagri = list(itertools.islice(uretec, 5))
ikinci_cagri = list(itertools.islice(uretec, 5))
print("Aynı üreteçten ilk 5 eleman :", ilk_cagri)
print("Aynı üreteçten ikinci 5 eleman:", ikinci_cagri)
