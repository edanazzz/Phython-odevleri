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
