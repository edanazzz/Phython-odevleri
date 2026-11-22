# Ad Soyad: Eda Naz Gülarslan
# Numara: 20253005006
# Tarih: 22.11.2026
# Açıklama: Özel metotlarla geliştirilmiş Kesir sınıfı (aritmetik, karşılaştırma ve float dönüşümü).

import math


class Kesir:
    """Kesirleri sade biçimde tutan, dört işlem ve karşılaştırma destekleyen sınıf."""

    def __init__(self, pay, payda=1):
        """Kesri oluşturur, işareti paya taşır ve EBOB ile sadeleştirir."""
        if payda == 0:
            raise ValueError("Payda sıfır olamaz.")
        if payda < 0:
            pay = -pay
            payda = -payda
        ebob = math.gcd(abs(pay), payda)
        self.pay = pay // ebob
        self.payda = payda // ebob

    def __str__(self):
        """Kesri okunabilir metin biçiminde döndürür."""
        if self.payda == 1:
            return str(self.pay)
        return f"{self.pay}/{self.payda}"

    def __add__(self, diger):
        """İki kesri toplar ve yeni sade bir Kesir döndürür."""
        yeni_pay = self.pay * diger.payda + diger.pay * self.payda
        yeni_payda = self.payda * diger.payda
        return Kesir(yeni_pay, yeni_payda)

    def __sub__(self, diger):
        """İki kesri çıkarır ve yeni sade bir Kesir döndürür."""
        yeni_pay = self.pay * diger.payda - diger.pay * self.payda
        yeni_payda = self.payda * diger.payda
        return Kesir(yeni_pay, yeni_payda)

    def __mul__(self, diger):
        """İki kesri çarpar ve yeni sade bir Kesir döndürür."""
        return Kesir(self.pay * diger.pay, self.payda * diger.payda)

    def __truediv__(self, diger):
        """İki kesri böler ve yeni sade bir Kesir döndürür."""
        return Kesir(self.pay * diger.payda, self.payda * diger.pay)

    def __eq__(self, diger):
        """İki kesrin eşitliğini çapraz çarpımla kontrol eder."""
        return self.pay * diger.payda == diger.pay * self.payda

    def __lt__(self, diger):
        """Küçüktür (<) karşılaştırmasını çapraz çarpımla yapar."""
        return self.pay * diger.payda < diger.pay * self.payda

    def __le__(self, diger):
        """Küçük veya eşittir (<=) karşılaştırmasını çapraz çarpımla yapar."""
        return self.pay * diger.payda <= diger.pay * self.payda

    def __float__(self):
        """Kesrin ondalıklı sayı (float) karşılığını döndürür."""
        return self.pay / self.payda


# Temel örnek testler
print("6/8 == 3/4:", Kesir(6, 8) == Kesir(3, 4))          # True
print("3/4 / 3/8:", Kesir(3, 4) / Kesir(3, 8))            # 2
print("float(1/4):", float(Kesir(1, 4)))                  # 0.25

# (a) Döngüyle çarpım: (1 - 1/2) * (1 - 1/3) * ... * (1 - 1/10)
carpim = Kesir(1, 1)
for n in range(2, 11):
    carpim = carpim * (Kesir(1, 1) - Kesir(1, n))
print("Çarpım:", carpim)                                  # 1/10

# (b) Yalnızca < kullanarak (ve liste kullanmadan) en büyük kesri bulma
en_buyuk = Kesir(3, 7)
k2 = Kesir(5, 12)
k3 = Kesir(2, 5)
k4 = Kesir(4, 9)
k5 = Kesir(3, 8)

if en_buyuk < k2:
    en_buyuk = k2
if en_buyuk < k3:
    en_buyuk = k3
if en_buyuk < k4:
    en_buyuk = k4
if en_buyuk < k5:
    en_buyuk = k5
print("En büyük:", en_buyuk)                              # 4/9

# Ek farklı testler
print("1/3 + 1/6:", Kesir(1, 3) + Kesir(1, 6))            # 1/2
print("2/5 <= 4/10:", Kesir(2, 5) <= Kesir(4, 10))        # True
