import sys
import os
from functools import lru_cache

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from uzay_oyunu.dekoratorler import sure_olc, say, log_cagri, sinirla, hafiza
from uzay_oyunu.komutlar import KOMUTLAR, komut

# --- GÖREV 1 TESTLERİ ---
@sure_olc
def topla(a, b): return a + b

def test_gorev1():
    assert topla(3, 4) == 7
    print("Görev 1 Testleri Başarılı.")

# --- GÖREV 2 TESTLERİ ---
@say
def ornek_sayici(): pass

def test_gorev2():
    ornek_sayici()
    assert ornek_sayici.cagri == 1
    print("Görev 2 Testi Başarılı.")

# --- GÖREV 3 TESTLERİ ---
@log_cagri
def test_yolculuk(): return "orion"

def test_gorev3():
    assert test_yolculuk() == "orion"
    print("Görev 3 Testi Başarılı.")

# --- GÖREV 4 TESTLERİ ---
def test_gorev4():
    assert "yardim" in KOMUTLAR
    print("Görev 4 Testleri Başarılı.")

# --- GÖREV 5 TESTLERİ ---
@sinirla(0, 100)
def yakit_harca(miktar):
    return 100 - miktar

def test_gorev5():
    assert yakit_harca(30) == 70
    try:
        yakit_harca(150)
    except ValueError:
        pass
    print("Görev 5 Testleri Başarılı.")

# --- BONUS GÖREV TESTLERİ ---
def test_bonus():
    # 1. Hazır lru_cache ile fonksiyon
    @lru_cache(maxsize=2)
    def kare_lru(x): return x * x

    # 2. Kendi yazdığımız hafıza ile fonksiyon
    @hafiza(maxsize=2)
    def kare_kendi(x): return x * x

    # İkisini de 3 farklı sayıyla çalıştıralım (Kapasiteleri 2)
    for i in (10, 20, 30):
        kare_lru(i)
        kare_kendi(i)

    # Kendi önbelleğimizde en eski olan '10' silinmiş, sadece '20' ve '30' kalmış olmalı
    kendi_onbellek = kare_kendi.cache_getir()
    assert (10,) not in kendi_onbellek
    assert (20,) in kendi_onbellek
    assert (30,) in kendi_onbellek
    
    print("Bonus Testi Başarılı: Kendi hafıza dekoratörümüz lru_cache gibi düzgün çalışıyor!")

if __name__ == "__main__":
    print("--- TÜM TESTLER BAŞLIYOR ---\n")
    test_gorev1()
    test_gorev2()
    test_gorev3()
    test_gorev4()
    test_gorev5()
    test_bonus()
    print("\n--- TEBRİKLER, TÜM GÖREVLER TAMAMLANDI! ---")
