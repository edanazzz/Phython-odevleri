import json

def galaksi_kur(gezegenler: list[str], baglantilar: dict, baslangic: str, **kwargs) -> dict:
    """JSON verisinden galaksiyi kurar ve başlangıç gezegenini doğrular."""
    
    # Başlangıç gezegeni listede yoksa hata fırlat (Ödevin kuralı)
    if baslangic not in gezegenler:
        raise ValueError(f"{baslangic} gezegeni gezegenler listesinde bulunamadı!")
    
    # Yakıt verilmemişse kwargs.get ile varsayılan 50 yap (Ödevin kuralı)
    yakit = kwargs.get("yakit", 50)
    
    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
    }

# Dosyayı okuyup fonksiyonu çalıştıran kod
if __name__ == "__main__":
    # galaksi.json dosyasını json.load ile okuma
    with open("uzay_oyunu/galaksi.json", "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)
        
    # Sözlüğü **veri biçiminde fonksiyona aktarma
    g = galaksi_kur(**veri)
    print("Kurulan Galaksi:", g["konum"], g["yakit"])
