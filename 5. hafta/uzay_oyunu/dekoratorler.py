# Kurum: İstanbul Nişantaşı Üniversitesi
# Ders: İleri Python Programlama
# Öğretim Üyesi: Dr. Öğr. Üyesi Murat Emeç
# Dönem: 2026-2027 Güz
# Öğrenci Adı Soyadı: EDA NAZ GÜLARSLAN
# Öğrenci Numarası: 20253005006
# Tarih: 23.10.2026
# Açıklama: Fonksiyonların çalışma süresini ölçen sure_olc dekoratörü.

import time
from functools import wraps

def sure_olc(fonk):
    """Bir fonksiyonun çalışma süresini ölçen dekoratör."""
    
    # wraps etiketi: İçerdeki asıl fonksiyonun adını ve kimliğini korumayı sağlar.
    @wraps(fonk)
    def sarmalayici(*args, **kwargs):
        # 1. Kronometreyi başlat:
        baslangic = time.perf_counter()
        
        # 2. Asıl fonksiyonu çalıştır ve sonucunu cebine koy:
        sonuc = fonk(*args, **kwargs)
        
        # 3. Kronometreyi durdur:
        bitis = time.perf_counter()
        
        # 4. Geçen süreyi hesapla ve ekrana yazdır:
        gecen_sure = bitis - baslangic
        print(f"{fonk.__name__}: {gecen_sure:.4f} sn")
        
        # 5. Asıl sonucu hiçbir şeye dokunmadan geri döndür:
        return sonuc
        
    return sarmalayici


def say(fonk):
    """Çağrı sayısını fonksiyonun bir niteliğinde (cagri) tutan dekoratör."""
    @wraps(fonk)
    def sarmalayici(*args, **kwargs):
        sarmalayici.cagri += 1  # Her çalışmada sayacı 1 artır
        return fonk(*args, **kwargs)
    
    # Sayacı başlangıçta 0 olarak ayarlıyoruz
    sarmalayici.cagri = 0
    return sarmalayici
def log_cagri(fonk):
    """Her çağrıdan önce argümanları, sonra dönüş değerini yazdıran dekoratör."""
    @wraps(fonk)
    def sarmalayici(*args, **kwargs):
        # 1. Gelen tüm argümanları metne çevirip aralarına virgül koyuyoruz
        arg_listesi = [repr(a) for a in args]
        kwarg_listesi = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        tum_argumanlar = ", ".join(arg_listesi + kwarg_listesi)
        
        # 2. Fonksiyon çalışmadan hemen önce ekrana yazdır (-> işaretiyle)
        print(f"-> {fonk.__name__}({tum_argumanlar})")
        
        # 3. Asıl fonksiyonu çalıştır ve sonucu al
        sonuc = fonk(*args, **kwargs)
        
        # 4. İşlem bittikten sonra sonucu ekrana yazdır (<- işaretiyle)
        print(f"<- {fonk.__name__} = {repr(sonuc)}")
        
        return sonuc
        
    return sarmalayici

