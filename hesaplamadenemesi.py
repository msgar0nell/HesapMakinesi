import tkinter as tk

history = []
user_actions = []

def calculate():
    try:
        operation = entry.get()
        result = eval(operation)
        result_label.config(text=f"Sonuç: {result}")

        operators = ["+", "-", "*", "/"]
        operator_count = sum(operation.count(op) for op in operators)

        if operator_count > 1: 
            action_type = "Çoklu İşlem"
        elif "+" in operation:
            action_type = "Toplama İşlemi"
        elif "-" in operation:
            action_type = "Çıkarma İşlemi"
        elif "*" in operation:
            action_type = "Çarpma İşlemi"
        elif "/" in operation:
            action_type = "Bölme İşlemi"
        else:
            action_type = "Bilinmeyen İşlem"

        history.append(f"{operation} = {result}")
        user_actions.append(f"Kullanıcı {action_type} Yaptı: {operation} = {result}")
    except Exception as e:
        result_label.config(text=f"Bir hata oluştu: {e}")

def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Geçmiş")
    history_window.geometry("400x300")

    history_label = tk.Label(history_window, text="Geçmiş", font=("Arial", 14))
    history_label.pack(pady=10)

    history_listbox = tk.Listbox(history_window, font=("Arial", 12), height=15, width=40)
    history_listbox.pack(pady=10)

    for item in history:
        history_listbox.insert(tk.END, item)

    close_button = tk.Button(history_window, text="Kapat", font=("Arial", 12), command=history_window.destroy)
    close_button.pack(pady=10)

def admin_panel():
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Paneli")
    admin_window.geometry("400x300")

    admin_label = tk.Label(admin_window, text="Admin Paneli", font=("Arial", 14))
    admin_label.pack(pady=10)

    admin_listbox = tk.Listbox(admin_window, font=("Arial", 12), height=15, width=40)
    admin_listbox.pack(pady=10)

    for action in user_actions:
        admin_listbox.insert(tk.END, action)
    
    close_button = tk.Button(admin_window, text="Kapat", font=("Arial", 12), command=admin_window.destroy)
    close_button.pack(pady=10)

def detaylar():
    detay_window = tk.Toplevel(root)
    detay_window.title("Detaylı Sekme")
    detay_window.geometry("640x480")

    detay_label = tk.Label(detay_window, text="Detaylı Sekme", font=("Arial", 14))
    detay_label.pack(pady=10)

    def creditdetay():
        credit_window = tk.Toplevel(detay_window)
        credit_window.title("Credit")
        credit_window.geometry("400x300")

        credit_label = tk.Label(credit_window, text="Credit", font=("Arial", 14))
        credit_label.pack(pady=10)
        
        credit_label_2 = tk.Label(credit_window, text="Doruk Eren Şimşek", font=("Arial", 14), anchor="center")
        credit_label_2.pack(pady=10)

        credit_label_3 = tk.Label(credit_window, text="Python", font=("Arial", 14), anchor="center")
        credit_label_3.pack(pady=10)

        credit_label_4 = tk.Label(credit_window, text="Tkinter Library", font=("Arial", 14), anchor="center")
        credit_label_4.pack(pady=10)

        credit_label_5 = tk.Label(credit_window, text="İlk Proje", font=("Arial", 14), anchor="center")
        credit_label_5.pack(pady=10)

    credit_button = tk.Button(detay_window, text="Credits", font=("Arial", 14), command=creditdetay)
    credit_button.pack(pady=10)

def open_buttons_window():
    buttons_window = tk.Toplevel(root)
    buttons_window.title("Düğmeler")
    buttons_window.geometry("300x400")

    def append_to_entry(value):
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text + str(value))

    numbers = [
        ("1", 1, 0), ("2", 1, 1), ("3", 1, 2),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
        ("7", 3, 0), ("8", 3, 1), ("9", 3, 2),
        ("0", 4, 1)
    ]

    for (text, row, col) in numbers:
        btn = tk.Button(buttons_window, text=text, font=("Arial", 14), width=5, height=2,
                        command=lambda t=text: append_to_entry(t))
        btn.grid(row=row, column=col, padx=5, pady=5)

    operators = ["+", "-", "*", "/"]
    for i, op in enumerate(operators):
        btn = tk.Button(buttons_window, text=op, font=("Arial", 14), width=5, height=2,
                        command=lambda o=op: append_to_entry(o))
        btn.grid(row=5, column=i, padx=5, pady=5)

root = tk.Tk()
root.title("Hesap Makinesi")
root.geometry("640x480")

label = tk.Label(root, text="Bir işlem giriniz", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 16), width=20)
entry.pack(pady=10)

calculate_button = tk.Button(root, text="Hesapla", font=("Arial", 14), width=15, height=2, command=calculate)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Sonuç", font=("Arial", 14))
result_label.pack(pady=10)

show_history_button = tk.Button(root, text="Geçmişi Göster", font=("Arial", 14), command=show_history)
show_history_button.pack(pady=10)

admin_button = tk.Button(root, text="Admin Panel", font=("Arial", 14), command=admin_panel)
admin_button.pack(pady=10)

detay_button = tk.Button(root, text="Detaylar", font=("Arial", 14), command=detaylar)
detay_button.pack(pady=10)

buttons_button = tk.Button(root, text="Düğmeler", font=("Arial", 14), command=open_buttons_window)
buttons_button.pack(pady=10)

root.mainloop()
