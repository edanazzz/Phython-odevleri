# Kurum: İstanbul Nişantaşı Üniversitesi
# Ders: Python ile Programlama
# Öğretim Üyesi: Dr. Öğr. Üyesi Murat Emeç
# Dönem: 2026-2027 Güz
# Öğrenci Adı Soyadı: EDA NAZ GÜLARSLAN
# Öğrenci Numarası: 20253005006
# Tarih: 18.10.2026
# Açıklama: Seyir defteri boru hattı üreteçleri (satirlari_oku, ayristir, uzun_yolculuklar).

def satirlari_oku(dosya_yolu: str):
    """Boş satırları ve # ile başlayan yorum satırlarını atlayarak üretir."""
    with open(dosya_yolu, "r", encoding="utf-8") as f:
        for satir in f:
            temiz = satir.strip()
            if temiz and not temiz.startswith("#"):
                yield temiz

def ayristir(satirlar):
    """Her satırdan (kaynak, hedef, yakit) demeti üretir."""
    for satir in satirlar:
        parcalar = satir.split()
        kaynak = parcalar[0]
        # parcalar[1] -> '->' ok simgesidir
        hedef = parcalar[2]
        yakit = int(parcalar[3])
        yield (kaynak, hedef, yakit)

def uzun_yolculuklar(kayitlar, esik: int):
    """Yakıtı eşik değerinden büyük olan yolculuk kayıtlarını süzer."""
    for kayit in kayitlar:
        if kayit[2] > esik:
            yield kayit

# --- Testler ---
dosya_yolu = "veri/seyir.txt"

# 1. Toplam yakıt hesabı testi:
toplam_yakit = sum(y for _, _, y in ayristir(satirlari_oku(dosya_yolu)))
print("Toplam Yakıt:", toplam_yakit)  # Beklenen çıktı: 88

# 2. Üreteç boru hattı üzerinden uzun yolculukları listeleme (örnek eşik: 12):
kayitlar = ayristir(satirlari_oku(dosya_yolu))
print("12'den büyük yolculuklar:", list(uzun_yolculuklar(kayitlar, 12)))
