# Ad Soyad: Eda Naz Gülarslan
# Numara: 20253005006
# Tarih: 01.11.2026
# Açıklama: Girilen 11 haneli string üzerinden T.C. Kimlik numarası geçerlilik kontrolü.

tc = input("T.C. kimlik no: ")

if len(tc) != 11 or not tc.isdigit() or tc[0] == '0':
    print(f"T.C. kimlik no: {tc} -> GEÇERSİZ")
else:
    tek_toplam = 0
    cift_toplam = 0
    
    # İlk 9 hanenin toplamı (İndeksler 0'dan başladığı için 0,2,4.. tek hanelerdir)
    for i in range(9):
        rakam = int(tc[i])
        if i % 2 == 0:
            tek_toplam += rakam
        else:
            cift_toplam += rakam

    # Kontrol hanelerinin hesaplanması
    h10 = (7 * tek_toplam - cift_toplam) % 10
    h11 = (tek_toplam + cift_toplam + h10) % 10

    # Hocanın örneğindeki çıktıyı aynen veriyoruz
    if h10 == int(tc[9]) and h11 == int(tc[10]):
        print(f"Tek: {tek_toplam} Çift: {cift_toplam} 10. hane: {h10} 11. hane: {h11} -> GEÇERLİ")
    else:
        print(f"T.C. kimlik no: {tc} -> GEÇERSİZ")
