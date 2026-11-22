# Ad Soyad: Eda Naz Gülarslan
# Numara: 20253005006
# Tarih: 22.11.2026
# Açıklama: Vigenère şifreleme ve çözme işlemini yapan program.

def vigenere(metin, anahtar, yon=1):
    """Verilen metni anahtar kelimeye göre Vigenère yöntemiyle şifreler (yon=1) veya çözer (yon=-1)."""
    anahtar = anahtar.upper()
    m = len(anahtar)
    sonuc = ""
    j = 0  # Anahtar harf sayacı (yalnızca harflerde ilerler)

    for ch in metin:
        if ("A" <= ch <= "Z") or ("a" <= ch <= "z"):
            baslangic = ord("A") if ch.isupper() else ord("a")
            p = ord(ch) - baslangic
            k = ord(anahtar[j % m]) - ord("A")
            yeni_harf = chr(baslangic + (p + yon * k) % 26)
            sonuc += yeni_harf
            j += 1
        else:
            sonuc += ch
    return sonuc


# Örnek testler
sifreli = vigenere("Attack at dawn", "LEMON")
print("Şifreli:", sifreli)                                # Lxfopv ef rnhr
print("Çözülmüş:", vigenere("Lxfopv ef rnhr", "LEMON", -1))  # Attack at dawn

# Ek farklı testler
test_sifreli = vigenere("Python 2026!", "KEY")
print("Ek test (şifreli):", test_sifreli)
print("Ek test (çözülmüş):", vigenere(test_sifreli, "KEY", -1))
