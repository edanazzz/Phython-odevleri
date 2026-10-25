# Kurum: İstanbul Nişantaşı Üniversitesi
# Öğrenci: EDA NAZ GÜLARSLAN (20253005006)
# Açıklama: Uzay oyunu komutları ve kayıt deseni (Görev 3 ve 4)

from uzay_oyunu.dekoratorler import log_cagri

# --- GÖREV 4: KOMUT SİSTEMİ (KAYIT DESENİ) ---
KOMUTLAR = {}

def komut(ad, aciklama=""):
    """Fonksiyonları KOMUTLAR sözlüğüne kaydeden dekoratör."""
    def sarmalayici(fonksiyon):
        # Aynı isimde iki komut eklenmeye çalışırsa hata fırlat
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' komutu zaten kayitli!")
        
        # Fonksiyonu hiç değiştirmeden (fonksiyon, aciklama) şeklinde sözlüğe kaydet
        KOMUTLAR[ad] = (fonksiyon, aciklama)
        return fonksiyon
    return sarmalayici

# Oyunun örnek durum sözlüğü (testler ve kullanım için)
ornek_durum = {
    "konum": "dünya",
    "baglantilar": {
        "dünya": ["centauri", "sirius", "orion"],
        "centauri": ["dünya", "orion"],
        "sirius": ["dünya", "orion"],
        "orion": ["dünya", "centauri", "sirius"],
        "kara_delik": []
    },
    "credits": 100,
    "engines": "Standart",
    "copilot": "Eda"
}

# 1. Yardım Komutu
@komut("yardim", "komutlari listeler")
def yardim_komutu(durum):
    for k_ad, (k_fonk, k_aciklama) in KOMUTLAR.items():
        print(f"{k_ad.ljust(10)} {k_aciklama}")

# 2. Envanter Komutu
@komut("envanter", "esyalarini gosterir")
def envanter_komutu(durum):
    print(f"Krediler: {durum.get('credits', 0)}")
    print(f"Motorlar: {durum.get('engines', 'Yok')}")
    print(f"Kopilot: {durum.get('copilot', 'Yok')}")

# 3. Harita Komutu
@komut("harita", "gidebilecegin gezegenleri gosterir")
def harita_komutu(durum):
    konum = durum.get("konum", "")
    baglantilar = durum.get("baglantilar", {})
    gidilebilir = baglantilar.get(konum, [])
    print(", ".join(gidilebilir))


# --- GÖREV 3'TEN KALANLAR ---
@log_cagri
def galaksi_kur():
    """Galaksi bağlantılarını kurar ve döndürür."""
    return ornek_durum["baglantilar"]

@log_cagri
def hedef_menusu(hedef_gezegen):
    """Seçilen hedef gezegen için menüyü gösterir."""
    return f"{hedef_gezegen.capitalize()} sistemine rota oluşturuluyor..."
