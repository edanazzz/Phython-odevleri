# Ders: Python ile Programlama
# Kurum: İstanbul Nişantaşı Üniversitesi
# Öğretim Üyesi: Dr. Öğr. Üyesi Murat Emeç
# Dönem: 2026-2027 Güz
# Öğrenci: Eda Naz Gülarslan
# Numara: 20253005006
# Teslim Tarihi: 04/10/2026

# Bonus Görev – Olimpiyat Halkaları
import turtle

cizici = turtle.Turtle()
cizici.speed(5)
cizici.pensize(5)

# Çember çizme fonksiyonu
def cember_ciz(x, y, renk):
    cizici.penup()
    cizici.goto(x, y)
    cizici.pendown()
    cizici.color(renk)
    cizici.circle(45)

# Üst sıra halkalar
cember_ciz(-110, 0, "blue")
cember_ciz(0, 0, "black")
cember_ciz(110, 0, "red")

# Alt sıra halkalar
cember_ciz(-55, -45, "yellow")
cember_ciz(55, -45, "green")

cizici.hideturtle()
turtle.done()
