# Kurum: İstanbul Nişantaşı Üniversitesi
# Öğrenci: EDA NAZ GÜLARSLAN (20253005006)
# Açıklama: Görev 4 - Ana oyun döngüsü ve komut sistemi entegrasyonu.

from uzay_oyunu.komutlar import KOMUTLAR, ornek_durum

def travel():
    print("--- UZAY MACERASINA HOŞ GELDİN ---")
    
    while True:
        konum = ornek_durum["konum"]
        baglantilar = ornek_durum.get("baglantilar", {})
        gidilebilir_gezegenler = baglantilar.get(konum, [])
        
        print("\nNereye gitmek istersin?")
        for i, gezegen in enumerate(gidilebilir_gezegenler, 1):
            print(f"[{i}] {gezegen}")
            
        girdi = input("> ").strip().lower()
        
        if not girdi:
            continue
            
        # 1. KONTROL: Girdi yeni yazdığımız komutlardan biri mi? (yardim, harita, envanter)
        if girdi in KOMUTLAR:
            fonksiyon, aciklama = KOMUTLAR[girdi]
            fonksiyon(ornek_durum)  # Komutu çalıştır
            continue                # Döngünün başına dön (menüyü tekrar göster)
            
        # 2. KONTROL: Girdi sayı ise gezegen seçimi olarak yorumla (eski mantık)
        if girdi.isdigit():
            secim_indeksi = int(girdi) - 1
            if 0 <= secim_indeksi < len(gidilebilir_gezegenler):
                yeni_konum = gidilebilir_gezegenler[secim_indeksi]
                ornek_durum["konum"] = yeni_konum
                print(f"-> {yeni_konum.capitalize()} gezegenine seyahat ediliyor...")
            else:
                print("Geçersiz rota numarası!")
        elif girdi == "cikis":
            print("Oyundan çıkılıyor...")
            break
        else:
            print("Bilinmeyen komut! Komutları görmek için 'yardim' yazabilirsiniz.")

if __name__ == "__main__":
    travel()
