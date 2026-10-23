import sys
import os
from functools import lru_cache
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from uzay_oyunu.dekoratorler import sure_olc, say


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
    print("\n--- GÖREV 2: FİBONACCİ ÇAĞRI SAYILARI ---")
    fib_yalnizca_say(20)
    print(f"Yalnızca @say: {fib_yalnizca_say.cagri}")
    
    fib_say_ustte(20)
    print(f"@say üstte, @lru_cache altta: {fib_say_ustte.cagri}")
    
    fib_cache_ustte(20)
    # lru_cache dışarıda olduğu için içindeki sayaca __wrapped__ ile ulaşıyoruz
    print(f"@lru_cache üstte, @say altta: {fib_cache_ustte.__wrapped__.cagri}")

    print("--- DEKORATÖR TESTLERİ ---\n")
    test_sonuc_degismiyor()
    test_adli_argumanlar()
    test_kimlik_korunuyor()
    
    print("\n--- HAFTA 4 ROTA SAYACI SÜRE ÖLÇÜMÜ (Adım=20) ---")
    rota_sayaci_baslat(galaksi_baglantilari, "dünya", 20)
# --- GÖREV 2: FİBONACCİ ÇAĞRI SAYACI TESTLERİ ---

# 1. Yalnızca @say
@say
def fib_yalnizca_say(n):
    if n < 2: return n
    return fib_yalnizca_say(n-1) + fib_yalnizca_say(n-2)

# 2. @say üstte, @lru_cache altta
@say
@lru_cache(maxsize=None)
def fib_say_ustte(n):
    if n < 2: return n
    return fib_say_ustte(n-1) + fib_say_ustte(n-2)

# 3. @lru_cache üstte, @say altta
@lru_cache(maxsize=None)
@say
def fib_cache_ustte(n):
    if n < 2: return n
    return fib_cache_ustte(n-1) + fib_cache_ustte(n-2)


