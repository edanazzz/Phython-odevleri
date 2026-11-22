# Ad Soyad: Eda Naz Gülarslan
# Numara: 20253005006
# Tarih: 22.11.2026
# Açıklama: Türkçe alfabe sırasına göre karşılaştırma ve büyük/küçük harf dönüşümü yapan TrKelime sınıfı.

ALFABE = "abcçdefgğhıijklmnoöprsştuüvyz"


class TrKelime:
    """Türkçe harf kurallarına göre işlem ve sıralama yapan kelime sınıfı."""

    def __init__(self, metin):
        """Metni Türkçe kurala göre küçülterek saklar (önce I->ı, İ->i)."""
        self.metin = metin.replace("I", "ı").replace("İ", "i").lower()

    def __str__(self):
        """Kelimenin metin karşılığını döndürür."""
        return self.metin

    def __len__(self):
        """Kelimenin karakter sayısını döndürür."""
        return len(self.metin)

    def __getitem__(self, indeks):
        """Verilen indeksteki harfi veya dilimi döndürür."""
        return self.metin[indeks]

    def __contains__(self, parca):
        """Verilen metin parçasının kelime içinde geçip geçmediğini kontrol eder."""
        aranan = parca.replace("I", "ı").replace("İ", "i").lower()
        return aranan in self.metin

    def __eq__(self, diger):
        """İki TrKelime nesnesinin eşitliğini kontrol eder."""
        return self.metin == diger.metin

    def __lt__(self, diger):
        """İki kelimeyi ALFABE.find ile harf harf karşılaştırır; ön ek durumunda kısa olan küçüktür."""
        sinir = min(len(self.metin), len(diger.metin))
        for i in range(sinir):
            if self.metin[i] != diger.metin[i]:
                return ALFABE.find(self.metin[i]) < ALFABE.find(diger.metin[i])
        return len(self.metin) < len(diger.metin)

    def buyuk(self):
        """Kelimeyi Türkçe kuralına göre büyük harfe çevirir (önce i->İ, ı->I)."""
        return self.metin.replace("i", "İ").replace("ı", "I").upper()


# Örnek testler (Türkçe vs Python str karşılaştırması)
print("çay < dağ     -> Türkçe:", TrKelime("çay") < TrKelime("dağ"), "| Python str:", "çay" < "dağ")
print("ılık < iğne   -> Türkçe:", TrKelime("ılık") < TrKelime("iğne"), "| Python str:", "ılık" < "iğne")
print("ördek < pasta -> Türkçe:", TrKelime("ördek") < TrKelime("pasta"), "| Python str:", "ördek" < "pasta")

print("Işık == ışık:", TrKelime("Işık") == TrKelime("ışık"))

k = TrKelime("İSTANBUL")
print("k:", k)                    # istanbul
print("len(k):", len(k))          # 8
print("'tan' in k:", "tan" in k)  # True
print("k.buyuk():", k.buyuk())    # İSTANBUL

# Ek farklı testler
print("çam < çamur (ön ek):", TrKelime("çam") < TrKelime("çamur"))  # True
print("k[0]:", k[0])                                                # i
