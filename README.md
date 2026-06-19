# 🔒 Secure File Locker Pro

A modern desktop application built with Python that allows users to securely encrypt and decrypt files using password-based AES encryption.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-green)
![License](https://img.shields.io/badge/License-MIT-orange)

---

## 📖 Overview

Secure File Locker Pro is a cybersecurity-focused desktop application that helps users protect sensitive files through strong encryption.

The application provides an intuitive graphical interface, password strength analysis, encryption history tracking, dark mode support, and recovery key generation.

---

## ✨ Features

### 🔐 Security

* AES-based file encryption
* Password-protected file locking
* Secure SHA-256 password hashing
* File decryption with password verification
* Recovery key generation
* Invalid password detection

### 🎨 User Interface

* Modern CustomTkinter GUI
* Dark / Light Mode
* Show / Hide Password
* Progress Bar
* File Size Display
* Responsive Layout

### 📁 File Management

* Select any file type
* Encrypt files instantly
* Decrypt encrypted files
* Encryption history tracking
* Local storage support

---

## 🖼️ Screenshot

Add your application screenshot here.

```text
screenshots/main_window.png
```

---

## 📂 Project Structure

```text
SecureFileLockerPro/

├── locker.py
├── history.json
├── icon.ico
├── README.md
│
└── screenshots/
    └── main_window.png
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/SecureFileLockerPro.git

cd SecureFileLockerPro
```

### Install Dependencies

```bash
pip install cryptography
pip install customtkinter
```

### Run Application

```bash
python locker.py
```

---

## 📦 Required Libraries

| Package       | Purpose                 |
| ------------- | ----------------------- |
| customtkinter | Modern GUI              |
| cryptography  | AES Encryption          |
| hashlib       | Password Hashing        |
| secrets       | Recovery Key Generation |
| json          | History Storage         |

---

## 🚀 Build Executable (.exe)

Install PyInstaller:

```bash
pip install pyinstaller
```

Build executable:

```bash
pyinstaller --onefile --windowed --icon=icon.ico locker.py
```

Output:

```text
dist/
└── locker.exe
```

---

## 🔑 How Encryption Works

1. User selects a file.
2. User enters a password.
3. Password is converted into a secure SHA-256 key.
4. AES encryption is applied.
5. Encrypted file is saved with:

```text
filename.ext.locked
```

6. Recovery key is generated.

---

## 📜 Example

Original file:

```text
secret.pdf
```

Encrypted file:

```text
secret.pdf.locked
```

---

## 📊 Future Improvements

### Version 2.0

* Drag & Drop Support
* Multi-File Encryption
* Folder Encryption
* Password Generator
* Secure File Deletion

### Version 3.0

* SQLite Database
* User Accounts
* Cloud Backup
* Automatic Updates

### Version 4.0

* Two-Factor Authentication
* Encrypted Vault System
* Secure Notes Manager
* Network File Sharing

---

## 🧠 Skills Demonstrated

This project demonstrates:

* Python Programming
* GUI Development
* Cybersecurity Concepts
* Cryptography
* File Handling
* JSON Data Storage
* Software Packaging

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Gaurav Singh**

Built with Python ❤️

If you found this project useful, please consider giving it a ⭐ on GitHub.
