# Ad Soyad: Eda Naz Gülarslan
# Numara: 20253005006
# Tarih: 01.11.2026
# Açıklama: Bonus Görev - Luhn algoritması ile eksik 15. haneyi bulma.

eksik_numara = "45391488934364"

for denenen_rakam in range(10):
    tam_numara = eksik_numara + str(denenen_rakam)
    toplam = 0
    
    # 15 haneli numarayı sağdan sola doğru (indeks 14'ten 0'a) okuyoruz
    for i in range(14, -1, -1):
        basamak_degeri = int(tam_numara[i])
        
        # Sağdan sola çift sıradaki (indeks olarak 13, 11, 9...) haneleri 2 ile çarpıyoruz
        if (14 - i) % 2 == 1:
            basamak_degeri *= 2
            if basamak_degeri > 9:
                basamak_degeri -= 9
                
        toplam += basamak_degeri
        
    # Toplam 10'un tam katıysa doğru kontrol hanesini bulduk demektir
    if toplam % 10 == 0:
        print(f"Doğru cevap (X): {denenen_rakam}")
        break
