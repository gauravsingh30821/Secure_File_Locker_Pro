import customtkinter as ctk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import hashlib
import base64
import os
import json
import secrets

app = ctk.CTk()

app.iconbitmap("c:\Users\10\Downloads\c5a90cc0-af0b-4b12-904f-0295f8bf60bc.ico")  # Your icon file
app.mainloop()

# ----------------------------
# CONFIG
# ----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

HISTORY_FILE = "history.json"

selected_file = None

# ----------------------------
# HELPERS
# ----------------------------

def generate_key(password):
    password = password.encode()
    key = hashlib.sha256(password).digest()
    return base64.urlsafe_b64encode(key)

def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(not c.isalnum() for c in password):
        score += 1

    return score

def generate_recovery_key():
    return secrets.token_hex(16)

def save_history(action, filename):
    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except:
        history = []

    history.append({
        "action": action,
        "file": filename
    })

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def update_strength(event=None):
    password = password_entry.get()

    score = password_strength(password)

    if score <= 2:
        strength_label.configure(
            text="Password Strength: Weak"
        )
    elif score <= 4:
        strength_label.configure(
            text="Password Strength: Medium"
        )
    else:
        strength_label.configure(
            text="Password Strength: Strong"
        )

# ----------------------------
# FILE SELECTION
# ----------------------------

def choose_file():
    global selected_file

    file_path = filedialog.askopenfilename()

    if not file_path:
        return

    selected_file = file_path

    file_label.configure(
        text=os.path.basename(file_path)
    )

    size = os.path.getsize(file_path)
    size_mb = size / (1024 * 1024)

    size_label.configure(
        text=f"Size: {size_mb:.2f} MB"
    )

# ----------------------------
# ENCRYPT
# ----------------------------

def encrypt_file():
    global selected_file

    if not selected_file:
        messagebox.showerror(
            "Error",
            "Please choose a file."
        )
        return

    password = password_entry.get()

    if not password:
        messagebox.showerror(
            "Error",
            "Enter a password."
        )
        return

    try:
        progress.set(0)

        key = generate_key(password)

        cipher = Fernet(key)

        with open(selected_file, "rb") as f:
            data = f.read()

        progress.set(0.3)
        app.update()

        encrypted_data = cipher.encrypt(data)

        progress.set(0.7)
        app.update()

        encrypted_file = selected_file + ".locked"

        with open(encrypted_file, "wb") as f:
            f.write(encrypted_data)

        progress.set(1)

        recovery = generate_recovery_key()

        save_history(
            "Encrypted",
            encrypted_file
        )

        messagebox.showinfo(
            "Success",
            f"File Encrypted!\n\nRecovery Key:\n{recovery}"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )

# ----------------------------
# DECRYPT
# ----------------------------

def decrypt_file():
    global selected_file

    if not selected_file:
        messagebox.showerror(
            "Error",
            "Choose encrypted file."
        )
        return

    password = password_entry.get()

    if not password:
        messagebox.showerror(
            "Error",
            "Enter password."
        )
        return

    try:
        progress.set(0)

        key = generate_key(password)

        cipher = Fernet(key)

        with open(selected_file, "rb") as f:
            encrypted_data = f.read()

        progress.set(0.5)
        app.update()

        decrypted_data = cipher.decrypt(
            encrypted_data
        )

        output_file = selected_file.replace(
            ".locked",
            ""
        )

        with open(output_file, "wb") as f:
            f.write(decrypted_data)

        progress.set(1)

        save_history(
            "Decrypted",
            output_file
        )

        messagebox.showinfo(
            "Success",
            "File Decrypted Successfully!"
        )

    except:
        messagebox.showerror(
            "Error",
            "Wrong Password or Invalid File"
        )

# ----------------------------
# HISTORY VIEWER
# ----------------------------

def view_history():

    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)

        text = ""

        for item in history:
            text += (
                f"{item['action']} -> "
                f"{item['file']}\n"
            )

        if not text:
            text = "No History Found"

        messagebox.showinfo(
            "History",
            text
        )

    except:
        messagebox.showinfo(
            "History",
            "No History Found"
        )

# ----------------------------
# PASSWORD TOGGLE
# ----------------------------

def toggle_password():

    if password_entry.cget("show") == "*":
        password_entry.configure(show="")
        show_btn.configure(text="Hide")
    else:
        password_entry.configure(show="*")
        show_btn.configure(text="Show")

# ----------------------------
# THEME TOGGLE
# ----------------------------

def toggle_theme():

    current = ctk.get_appearance_mode()

    if current == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

# ----------------------------
# GUI
# ----------------------------

app = ctk.CTk()

app.title("Secure File Locker Pro")

app.geometry("700x650")

title = ctk.CTkLabel(
    app,
    text="🔒 Secure File Locker Pro",
    font=("Arial", 28, "bold")
)

title.pack(pady=20)

theme_btn = ctk.CTkButton(
    app,
    text="Toggle Theme",
    command=toggle_theme
)

theme_btn.pack(pady=5)

choose_btn = ctk.CTkButton(
    app,
    text="Choose File",
    command=choose_file
)

choose_btn.pack(pady=10)

file_label = ctk.CTkLabel(
    app,
    text="No File Selected"
)

file_label.pack()

size_label = ctk.CTkLabel(
    app,
    text="Size: 0 MB"
)

size_label.pack(pady=5)

password_entry = ctk.CTkEntry(
    app,
    width=300,
    show="*",
    placeholder_text="Enter Password"
)

password_entry.pack(pady=15)

password_entry.bind(
    "<KeyRelease>",
    update_strength
)

show_btn = ctk.CTkButton(
    app,
    text="Show",
    width=100,
    command=toggle_password
)

show_btn.pack()

strength_label = ctk.CTkLabel(
    app,
    text="Password Strength: "
)

strength_label.pack(pady=10)

encrypt_btn = ctk.CTkButton(
    app,
    text="Encrypt File",
    command=encrypt_file
)

encrypt_btn.pack(pady=10)

decrypt_btn = ctk.CTkButton(
    app,
    text="Decrypt File",
    command=decrypt_file
)

decrypt_btn.pack(pady=10)

history_btn = ctk.CTkButton(
    app,
    text="View History",
    command=view_history
)

history_btn.pack(pady=10)

progress = ctk.CTkProgressBar(
    app,
    width=400
)

progress.pack(pady=25)

progress.set(0)

footer = ctk.CTkLabel(
    app,
    text="Created with Python + CustomTkinter"
)

footer.pack(side="bottom", pady=20)

app.mainloop()