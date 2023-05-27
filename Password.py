    # ГЕНЕРАТОР ПАРОЛЕЙ И ОРГАНАЙЗЕР ДЛЯ ХРАНЕНИЯ ПАРОЛЕЙ

import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def generate_password(length, include_letters, include_digits, include_special_chars, include_uncommon_chars):
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    if include_uncommon_chars:
        characters += '№@§$%&*_-=+'

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def check_password_complexity(password):
    # Проверка  пароля на сложность
    if len(password) < 6 or password.isalpha() or password.isnumeric():
        return False
    return True

def save_password(password):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(password)
            messagebox.showinfo("Успешно", "Пароль сохранен в файл.")
        except IOError:
            messagebox.showerror("Ошибка", "Не удалось сохранить пароль в файл.")

def generate_password_button_clicked():
    length = int(length_entry.get())
    include_letters = include_letters_var.get()
    include_digits = include_digits_var.get()
    include_special_chars = include_special_chars_var.get()
    include_uncommon_chars = include_uncommon_chars_var.get()

    password = generate_password(length, include_letters, include_digits, include_special_chars, include_uncommon_chars)

    if check_password_complexity(password):
        password_label.config(text=f"Сгенерированный пароль: {password}")
        save_password_button.config(state=tk.NORMAL)
    else:
        password_label.config(text="Сгенерированный пароль не соответствует требованиям сложности.")
        save_password_button.config(state=tk.DISABLED)

def save_password_button_clicked():
    password = password_label.cget("text").split(": ")[1].strip()
    save_password(password)

window = tk.Tk()
window.title("Генератор паролей и органайзер для хранения паролей")
window.configure(bg="black")
window.geometry("600x350")

length_label = tk.Label(window, text="Длина пароля:", fg="white", bg="black", font=("Bahnschrift SemiBold", 16))
length_label.pack()

length_entry = tk.Entry(window, font=("GOST type A", 16))
length_entry.pack()

include_letters_var = tk.BooleanVar()
include_digits_var = tk.BooleanVar()
include_special_chars_var = tk.BooleanVar()
include_uncommon_chars_var = tk.BooleanVar()

include_letters_checkbox = tk.Checkbutton(window, text="Включать буквы", variable=include_letters_var, fg="cyan", bg="black", font=("GOST type A", 18))
include_letters_checkbox.pack()

include_digits_checkbox = tk.Checkbutton(window, text="Включать цифры", variable=include_digits_var, fg="cyan", bg="black", font=("GOST type A", 18))
include_digits_checkbox.pack()

include_special_chars_checkbox = tk.Checkbutton(window, text="Включать специальные символы", variable=include_special_chars_var, fg="blue", bg="black", font=("Corbel Light", 14))
include_special_chars_checkbox.pack()

include_uncommon_chars_checkbox = tk.Checkbutton(window, text="Включать необычные символы", variable=include_uncommon_chars_var, fg="blue", bg="black", font=("Corbel Light", 14))
include_uncommon_chars_checkbox.pack()

generate_button = tk.Button(window, text="Сгенерировать пароль", command=generate_password_button_clicked, fg="cyan", bg="black", font=("GOST type A", 16))
generate_button.pack()

password_label = tk.Label(window, text="", fg="cyan", bg="black", font=("GOST type A", 16))
password_label.pack()

save_password_button = tk.Button(window, text="Сохранить пароль", command=save_password_button_clicked, fg="cyan", bg="black", font=("GOST type A", 16), state=tk.DISABLED)
save_password_button.pack()

window.mainloop()
