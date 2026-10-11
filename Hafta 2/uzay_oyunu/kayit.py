def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: str):
    """Görev bilgilerini ve adımlarını ekrana yazdırır."""
    
    # Başlığı ve önceliği yazdır (Öncelik büyük harfle istenmiş)
    print(f"[{oncelik.upper()}] {baslik}")
    
    # Sınırsız sayıda gelebilen adımları numaralandırarak yazdır
    for i, adim in enumerate(adimlar, start=1):
        print(f"{i}. {adim}")
        
    # Ekstra olarak gönderilen sözlük verilerini yazdır
    for anahtar, deger in ekler.items():
        print(f"{anahtar}: {deger}")

# Modül doğrudan çalıştırıldığında test etmek için main bloğu
if __name__ == "__main__":
    # Test verilerimiz
    adimlar_listesi = ["Kredi kazan", "Pilot bul", "Yakıt deposunu doldur"]
    ekler_sozlugu = {"sorumlu": "Ayşe"}
    
    # Bir listeyi (*) ve bir sözlüğü (**) açarak fonksiyonu çağırma
    gorev_kaydi(
        "Kara deliğe atla", 
        *adimlar_listesi, 
        oncelik="yüksek", 
        **ekler_sozlugu
    )
