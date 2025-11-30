# 🔒 Secure File Sharing System (E2EE)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Web Crypto API](https://img.shields.io/badge/Web%20Crypto%20API-Standard-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A secure file sharing application that implements **End-to-End Encryption (E2EE)**. Files are encrypted in the browser using the Web Crypto API (AES-GCM) before upload. The server stores only the encrypted blob and never sees the decryption key.

## 🧐 The Problem

Traditional file sharing services often have access to your data. Even if they use encryption, they usually hold the keys, meaning they (or hackers who breach them) can read your files.

## 💡 The Solution

This system uses a **Zero-Knowledge** architecture:
1.  **Client-Side Encryption**: Your browser generates a unique key and encrypts the file *before* sending it.
2.  **Key in URL Fragment**: The decryption key is part of the share link's "hash" (`#key=...`). Browsers **never** send the hash to the server.
3.  **Dumb Storage**: The server only sees encrypted garbage. It cannot decrypt the file even if it wanted to.

## 🚀 Features

- **AES-GCM Encryption**: Industry-standard authenticated encryption.
- **Zero-Knowledge Server**: The server has zero knowledge of the file contents or keys.
- **One-Click Sharing**: Generates a secure link containing the key.
- **In-Browser Decryption**: No software installation required for the receiver.

## 🛠️ Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/CyberShuriken/secure-file-share.git
    cd secure-file-share
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

1.  **Start the Server**:
    ```bash
    python app.py
    ```

2.  **Open in Browser**:
    Go to `http://localhost:5000`.

3.  **Upload a File**:
    - Select a file and click "Encrypt & Upload".
    - Copy the generated link (e.g., `http://localhost:5000/file/uuid#key=...`).

4.  **Download**:
    - Open the link in a different browser or Incognito window.
    - Click "Decrypt & Download" to retrieve the original file.

## 🧠 Skills Demonstrated

- **Cryptography**: Implementing AES-GCM encryption/decryption using the Web Crypto API.
- **Web Security**: Understanding URL fragment security and client-side vs. server-side trust models.
- **Full-Stack Development**: Coordinating complex logic between a Python backend and JavaScript frontend.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
