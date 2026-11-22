# Ad Soyad: Eda Naz Gülarslan
# Numara: 20253005006
# Tarih: 22.11.2026
# Açıklama: E-posta adresini str metotları ile doğrulayan program.

def eposta_denetle(adres):
    """Verilen e-posta adresini kurallara göre denetler ve durum mesajı döndürür."""
    # 1. Kural: Tam olarak bir @ olmalı
    if adres.count("@") != 1:
        return "Tam olarak bir @ olmalı"

    # @ konumunu bul ve kullanıcı adı ile alan adını dilimle
    at_konum = adres.find("@")
    kullanici = adres[:at_konum]
    alan_adi = adres[at_konum + 1:]

    # 2. Kural: @ öncesi boş olmamalı ve yalnızca harf, rakam, '.', '_', '-' içermeli
    if len(kullanici) == 0:
        return "Kullanıcı adı boş olamaz"
    for ch in kullanici:
        if not (ch.isalnum() or ch in "._-"):
            return f"Geçersiz karakter: {ch}"

    # 3. Kural: Kullanıcı adı nokta ile başlayıp bitemez
    if kullanici.startswith(".") or kullanici.endswith("."):
        return "Nokta ile başlayamaz/bitemez"

    # 4. Kural: Alan adında en az bir nokta olmalı, nokta ile başlayıp bitemez
    if "." not in alan_adi or alan_adi.startswith(".") or alan_adi.endswith("."):
        return "Alan adı hatalı"

    # 5. Kural: Adreste boşluk olmamalı
    if " " in adres:
        return "Geçersiz karakter:  "

    return "Geçerli"

# Testler
print(eposta_denetle("ece.solmaz@nisantasi.edu.tr"))  # Geçerli
print(eposta_denetle("ece@@mail.com"))                # Tam olarak bir @ olmalı
print(eposta_denetle("ece solmaz@mail.com"))          # Geçersiz karakter:  
print(eposta_denetle(".ece@mail.com"))                # Nokta ile başlayamaz/bitemez
print(eposta_denetle("ece@mail"))                     # Alan adı hatalı
print(eposta_denetle("eda_naz@mail.com.tr"))          # Ek test: Geçerli
