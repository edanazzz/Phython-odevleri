import sys
import os

# Dekoratoru bulabilmesi için dosya yolunu ayarlıyoruz
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from uzay_oyunu.dekoratorler import sure_olc

# --- 1. Testler İçin Örnek Fonksiyonlar ---
@sure_olc
def topla(a, b):
    """İki sayıyı toplar."""
    return a + b

@sure_olc
def selamla(isim, mesaj="Merhaba"):
    """Kişiyi selamlar."""
    return f"{mesaj}, {isim}!"

# --- 2. İstenen 3 Testin Yapılması ---
def test_sonuc_degismiyor():
    assert topla(3, 4) == 7
    print("Test 1 Başarılı: Sonuç değişmeden dönüyor.")

def test_adli_argumanlar():
    assert selamla(isim="Eda", mesaj="Selam") == "Selam, Eda!"
    print("Test 2 Başarılı: Adlı argümanlarla çağrı çalışıyor.")

def test_kimlik_korunuyor():
    assert topla.__name__ == "topla"
    assert topla.__doc__ == "İki sayıyı toplar."
    print("Test 3 Başarılı: __name__ ve __doc__ korunuyor.")

# --- 3. Hafta 4 Önbelleksiz Rota Sayacı Süre Ölçümü ---
galaksi_baglantilari = {
    "dünya": ["centauri", "sirius", "orion"],
    "centauri": ["dünya", "orion"],
    "sirius": ["dünya", "orion"],
    "orion": ["dünya", "centauri", "sirius"],
    "kara_delik": []
}

def rota_sayisi_hesapla(baglantilar, gezegen, adim):
    if adim == 0:
        return 1
    toplam = 0
    for komsu in baglantilar.get(gezegen, []):
        toplam += rota_sayisi_hesapla(baglantilar, komsu, adim - 1)
    return toplam

# Sadece ana çağrının süresini ölçmek için sarmalıyoruz
@sure_olc
def rota_sayaci_baslat(baglantilar, gezegen, adim):
    return rota_sayisi_hesapla(baglantilar, gezegen, adim)

if __name__ == "__main__":
    print("--- DEKORATÖR TESTLERİ ---\n")
    test_sonuc_degismiyor()
    test_adli_argumanlar()
    test_kimlik_korunuyor()
    
    print("\n--- HAFTA 4 ROTA SAYACI SÜRE ÖLÇÜMÜ (Adım=20) ---")
    rota_sayaci_baslat(galaksi_baglantilari, "dünya", 20)
