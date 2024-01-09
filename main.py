

import tkinter as tk

def hesapla():
    ilaclar = {'aspirin': 5, 'koraskin': 10, 'vas': 15, 'parin': 20}
    tc_kimlik = tc_entry.get().strip()
    ilac_adlari = ilac_entry.get("1.0", tk.END).strip().splitlines()

    total_fiyat = 0
    for ilac in ilac_adlari:
        if ilac.lower() in ilaclar:
            total_fiyat += ilaclar[ilac.lower()]

    total_label.config(text="total : {} TL".format(total_fiyat))


root = tk.Tk()
root.title("Reçete Yönetim Sistemi")


tc_label = tk.Label(root, text="TC :")
tc_label.pack()
tc_entry = tk.Entry(root)
tc_entry.pack()


ilac_label = tk.Label(root, text="İlaç Adları :")
ilac_label.pack()
ilac_entry = tk.Text(root, height=4, width=30)
ilac_entry.pack()


hesapla_button = tk.Button(root, text="Hesapla", command=hesapla)
hesapla_button.pack()


total_label = tk.Label(root, text="Toplam Fiyat: 0 TL")
total_label.pack()

# Main loop
root.mainloop()
