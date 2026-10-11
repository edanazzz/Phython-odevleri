# Hatalı fonksiyon: Liste her çağrıda hafızada kalır (Tuzak)
def yakit_ekle_hatali(miktar, depo=[]):
    depo.append(miktar)
    return depo

def test_hatali_fonksiyon():
    yakit_ekle_hatali(10)
    # İkinci çağrıda sadece [20] bekleriz ama eski 10 da içinde kalır, test başarısız olur!
    sonuc = yakit_ekle_hatali(20)
    assert sonuc != [20] 

# Düzeltilmiş fonksiyon: None kalıbı kullanımı
def yakit_ekle(miktar, depo=None):
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo

def test_duzeltilmis_fonksiyon():
    assert yakit_ekle(10) == [10]
    assert yakit_ekle(20) == [20]  # Artık her seferinde sıfır depo açılır
