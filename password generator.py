import tkinter as tk
import secrets
import string

def generate_password():
    num_letters = int(letter_entry.get())
    num_digits = int(digit_entry.get())
    num_special_chars = int(special_char_entry.get())

    letters = ''.join(secrets.choice(string.ascii_letters) for _ in range(num_letters))
    digits = ''.join(secrets.choice(string.digits) for _ in range(num_digits))
    special_chars = ''.join(secrets.choice(string.punctuation) for _ in range(num_special_chars))

    password = list(letters + digits + special_chars)
    secrets.SystemRandom().shuffle(password)
    password = ''.join(password)

    password_label.config(text=password)

window = tk.Tk()
window.title("Password Generator")

letter_label = tk.Label(window, text="Enter number of letters:",width =50,height=3)
letter_label.pack()

letter_entry = tk.Entry(window)
letter_entry.pack()

digit_label = tk.Label(window, text="Enter number of digits:",width =50,height=3)
digit_label.pack()

digit_entry = tk.Entry(window)
digit_entry.pack()

special_char_label = tk.Label(window, text="Enter number of special characters:",width =50,height=3)
special_char_label.pack()

special_char_entry = tk.Entry(window)
special_char_entry.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(window, text="")
password_label.pack()

window.mainloop()