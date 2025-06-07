import tkinter as tk
import math

def butona_basma(deger):
    mevcut = ekran.get()
    ekran.delete(0, tk.END)
    ekran.insert(0, mevcut + deger)

def temizle():
    ekran.delete(0, tk.END)

def hesapla():
    ifade = ekran.get()
    try:
        if ifade.endswith("!"):
            sayi = int(ifade[:-1])
            sonuc = math.factorial(sayi)
        elif ifade.startswith("√"):
            sayi = float(ifade[1:])
            sonuc = math.sqrt(sayi)
        elif ifade.startswith("∛"):
            sayi = float(ifade[1:])
            sonuc = round(sayi ** (1/3), 6)
        else:
            sonuc = eval(ifade)
        ekran.delete(0, tk.END)
        ekran.insert(0, str(sonuc))
    except Exception:
        ekran.delete(0, tk.END)
        ekran.insert(0, "Hata")

pencere = tk.Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("600x750")  # Yüksekliği artırdım
pencere.configure(bg="#2e2e2e")

font_ekran = ("Arial", 24)
font_buton = ("Arial", 20, "bold")

ekran = tk.Entry(pencere, font=font_ekran, bg="#555555", fg="#f0f0f0", bd=0, justify="right", insertbackground="#f0f0f0")
ekran.pack(fill="x", pady=15, padx=10, ipady=15)

frame = tk.Frame(pencere, bg="#2e2e2e")
frame.pack()

butonlar = [
    ("1", "2", "3", "+"),
    ("4", "5", "6", "-"),
    ("7", "8", "9", "*"),
    ("0", ".", "%", "/"),
    ("!", "√", "³√", "C")
]

for i, satir in enumerate(butonlar):
    for j, deger in enumerate(satir):
        btn = tk.Button(frame, text=deger, font=font_buton, bg="#444444", fg="#ffffff", 
                        activebackground="#666666", activeforeground="#ffffff",
                        width=5, height=2,  # Buton genişliği artırıldı
                        command=lambda d=deger: butona_basma(d))
        btn.grid(row=i, column=j, padx=6, pady=6)  # Boşluk artırıldı

ozel_frame = tk.Frame(pencere, bg="#2e2e2e")
ozel_frame.pack(pady=15)

btn_hesapla = tk.Button(pencere, text="=", font=font_buton, bg="#4477aa", fg="#ffffff",
                        activebackground="#5599cc", activeforeground="#ffffff",
                        width=23, height=3,  # Buton genişliği ve yüksekliği artırıldı
                        command=hesapla)
btn_hesapla.pack(pady=15)

pencere.mainloop()
