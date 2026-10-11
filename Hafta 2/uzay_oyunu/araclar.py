import time

# Görev 5: Closure örneği
def hamle_sayaci():
    """Her çağrıldığında değeri bir artan bir sayaç fonksiyonu döndürür."""
    sayac = 0
    def artir():
        nonlocal sayac
        sayac += 1
        return sayac
    return artir

# Görev 5: Lambda ve Sıralama
def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sırayla döndürür."""
    baglantilar = galaksi.get("baglantilar", {})
    gezegenler = galaksi.get("gezegenler", [])
    
    # Sıralama kriteri: önce bağlantı sayısı (azalan için eksi), sonra harf sırası
    sirali = sorted(gezegenler, key=lambda p: (-len(baglantilar.get(p, [])), p))
    return sirali

# Bonus: Süre Ölçer Sarmalayıcı (Wrapper)
def sure_olc(fonksiyon):
    """Verilen fonksiyonun çalışma süresini ölçen sarmalayıcı döndürür."""
    def sarmalayici(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"{fonksiyon.__name__} çalışma süresi: {bitis - baslangic:.6f} saniye")
        return sonuc
    return sarmalayici

# Test Bloğu
if __name__ == "__main__":
    # Closure Testi
    say = hamle_sayaci()
    print("1. yolculuk sonrası:", say())
    print("2. yolculuk sonrası:", say())

    # Lambda, Sıralama ve Süre Ölçme Testi
    g_veri = {
        "gezegenler": ["dünya", "mars", "centauri", "sirius", "orion", "kara_delik"],
        "baglantilar": {
            "dünya": ["mars", "centauri"],
            "mars": ["dünya", "sirius"],
            "centauri": ["dünya", "orion"],
            "sirius": ["mars", "kara_delik"],
            "orion": ["centauri", "kara_delik"],
            "kara_delik": ["sirius", "orion"]
        }
    }
    
    # en_bagli_gezegenler fonksiyonunu sure_olc ile sarmalıyoruz
    en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)
    print("Sıralanmış Liste:", en_bagli_gezegenler(g_veri))
