# Kurum: İstanbul Nişantaşı Üniversitesi
# Öğrenci: EDA NAZ GÜLARSLAN (20253005006)
# Açıklama: Uzay oyunu komutları ve log_cagri entegrasyonu.

from uzay_oyunu.dekoratorler import log_cagri

@log_cagri
def galaksi_kur():
    """Galaksi bağlantılarını kurar ve döndürür."""
    baglantilar = {
        "dünya": ["centauri", "sirius", "orion"],
        "centauri": ["dünya", "orion"],
        "sirius": ["dünya", "orion"],
        "orion": ["dünya", "centauri", "sirius"],
        "kara_delik": []
    }
    return baglantilar

@log_cagri
def hedef_menusu(hedef_gezegen):
    """Seçilen hedef gezegen için menüyü gösterir."""
    mesaj = f"{hedef_gezegen.capitalize()} sistemine rota oluşturuluyor..."
    return mesaj

if __name__ == "__main__":
    # Test amaçlı çalıştırma
    print("--- KOMUTLAR TESTİ ---")
    sistem = galaksi_kur()
    hedef_menusu("orion")
