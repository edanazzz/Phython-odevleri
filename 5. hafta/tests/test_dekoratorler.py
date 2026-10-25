import sys
import os
from functools import lru_cache

# Dekoratorleri ve komutlari bulabilmesi için yol ayarı
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from uzay_oyunu.dekoratorler import sure_olc, say, log_cagri
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

# --- GÖREV 4 TESTLERİ (YENİ) ---
def test_gorev4():
    # 1. Komutlar kaydedilmiş mi?
    assert "yardim" in KOMUTLAR
    assert "envanter" in KOMUTLAR
    assert "harita" in KOMUTLAR
    
    # 2. Aynı isimde komut eklenirse hata veriyor mu?
    hata_verdi_mi = False
    try:
        @komut("yardim", "Kopya komut")
        def sahte_fonksiyon(durum): pass
    except ValueError:
        hata_verdi_mi = True
        
    assert hata_verdi_mi, "Aynı isimli komut engellenmedi!"
    print("Görev 4 Testleri Başarılı: Kayıt deseni ve hata fırlatma çalışıyor.")

if __name__ == "__main__":
    print("--- TÜM TESTLER BAŞLIYOR ---\n")
    test_gorev1()
    test_gorev2()
    test_gorev3()
    test_gorev4()
    print("\n--- TESTLER TAMAMLANDI ---")
