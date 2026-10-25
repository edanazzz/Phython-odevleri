import sys
import os
from functools import lru_cache

# Yol ayarları ve tüm dekoratörlerin içe aktarılması
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from uzay_oyunu.dekoratorler import sure_olc, say, log_cagri, sinirla
from uzay_oyunu.komutlar import KOMUTLAR, komut

# --- GÖREV 1 TESTLERİ ---
@sure_olc
def topla(a, b): return a + b

def test_gorev1():
    assert topla(3, 4) == 7
    assert topla.__name__ == "topla"
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
    hata_verdi_mi = False
    try:
        @komut("yardim", "Kopya")
        def sahte(durum): pass
    except ValueError:
        hata_verdi_mi = True
    assert hata_verdi_mi
    print("Görev 4 Testleri Başarılı.")

# --- GÖREV 5 TESTLERİ (YENİ) ---
@sinirla(0, 100)
def yakit_harca(miktar):
    return 100 - miktar

def test_gorev5():
    # 1. Normal ve sınır değerleri testleri (0 ve 100)
    assert yakit_harca(30) == 70
    assert yakit_harca(0) == 100
    assert yakit_harca(100) == 0
    
    # 2. Aralık dışı değer testi (150)
    hata_verdi_mi = False
    try:
        yakit_harca(150)
    except ValueError as e:
        hata_verdi_mi = True
        # Hata mesajının doğruluğunu kontrol ediyoruz
        assert str(e) == "yakit_harca: 150 değeri 0-100 aralığında değil"
        
    assert hata_verdi_mi, "Aralık dışı değerde hata fırlatılmadı!"
    print("Görev 5 Testleri Başarılı: Argüman alan sınır dekoratörü çalışıyor.")


if __name__ == "__main__":
    print("--- TÜM TESTLER BAŞLIYOR ---\n")
    test_gorev1()
    test_gorev2()
    test_gorev3()
    test_gorev4()
    test_gorev5()
    print("\n--- TESTLER TAMAMLANDI ---")
