# Ders: Python ile Programlama
# Kurum: İstanbul Nişantaşı Üniversitesi
# Öğretim Üyesi: Dr. Öğr. Üyesi Murat Emeç
# Dönem: 2026-2027 Güz
# Öğrenci: Eda Naz Gülarslan
# Numara: 20253005006
# Teslim Tarihi: 04/10/2026

# Görev 5 – Turtle ile Ev
import turtle

cizici = turtle.Turtle()
cizici.speed(5)

# Evin gövdesi (Kare)
for _ in range(4):
    cizici.forward(100)
    cizici.left(90)

# Çatıyı oturtmak için sol üst köşeye çıkış
cizici.penup()
cizici.goto(0, 100)
cizici.setheading(0)  # Sağa yönel
cizici.pendown()

# Üçgen çatı
cizici.left(60)
cizici.forward(100)
cizici.right(120)
cizici.forward(100)

# İsmi evin ortasına yazma
cizici.penup()
cizici.goto(25, 40)
cizici.pendown()
cizici.write("Edanaz", font=("Arial", 12, "normal"))

cizici.hideturtle()
turtle.done()
