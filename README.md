
# GenPhicoinWallet

A simple **Phicoin wallet generator** with a GUI built using Python's Tkinter library. This tool allows users to generate **private keys, public keys, and Phicoin addresses**. The generated wallet information is saved in `wallet.txt` for easy access and backup.

## ✨ Features

- Generate **Phicoin addresses**.
- Save wallet information (private key, public key, and address) in `wallet.txt`.
- User-friendly **GUI** for generating wallets.
- **WIF format** private key compatible with Bitcoin-like systems.

---

## 📦 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/genPhicoinWallet.git
   cd genPhicoinWallet
   ```

2. **Install the Required Dependencies**:
   Ensure Python is installed, then install the required packages using:
   ```bash
   sudo apt install python3-tk -y
   pip install ecdsa base58
   ```

---

## 🚀 Usage

1. **Run the Wallet Generator**:
   ```bash
   python wallet_generator.py
   ```

2. **Generate a Wallet**:
   - Enter random characters (optional) for entropy in the GUI.
   - Click **"Generate Wallet"** to generate a new Phicoin address.
   - The wallet details will be saved in `wallet.txt` in the current directory.

3. **View Wallet Details**:
   - The generated **Phicoin address** will be displayed in the GUI.
   - Check `wallet.txt` for:
     - Private key (in hexadecimal)
     - WIF private key
     - Public key (compressed and uncompressed)
     - Phicoin address

---

## 📝 Example Output (wallet.txt)

```
Private Key     : e9873d79c6dxxxxxxxe8b6c13f3e4f33e4f97
Private Key WIF : L1aW4aubDxxxxx1eR5ZkTnd
Public Key      : 038d95b86xxxxxxxd1234
Phicoin Address : P1abcdxxxxxxx67890
Uncompressed Public Key : 04axxxxxxxf90
```

---

## 📋 Requirements

- **Python 3.10**
- **Dependencies**: Install via `pip`:
  ```bash
  pip install ecdsa base58
  ```

---

## 💻 Convert to `.exe` (Optional)

If you want to distribute the tool as a **standalone executable**:

1. Install **PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. Generate the executable:
   ```bash
   pyinstaller --onefile --noconsole wallet_generator.py
   ```

3. The executable will be located in the `dist/` folder.

---

## 🛠️ Troubleshooting

- **Missing Dependencies**: Run `pip install ecdsa base58` to ensure all dependencies are installed.
- **GUI Not Launching**: Ensure you have Python 3.x installed.

---

## 🤝 Contributing

Feel free to open issues or submit pull requests to improve the tool.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 📧 Contact

For questions or feedback, contact us at **devteam@phicoin.net** or open an issue on the [GitHub repository](https://github.com/PhicoinProject/genPhicoinWallet).
