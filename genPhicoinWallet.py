import ecdsa
from base58 import b58encode
from hashlib import new as hashnew, sha256
import secrets
import tkinter as tk
from tkinter import messagebox

def doublehash(s):
    return sha256(sha256(s).digest()).digest()

def hash160(s):
    return hashnew('ripemd160', sha256(s).digest()).digest()

def doublehash_base58_checksum(s):
    return b58encode(s + doublehash(s)[:4]).decode("utf-8")

def generate_wallet():
    # Generate a 256-bit random number as the private key
    private_key = secrets.randbits(256).to_bytes(32, "big")

    # Convert the private key to WIF format with prefix 0x80 (Bitcoin standard)
    wif = doublehash_base58_checksum(b'\x80' + private_key + b'\x01')

    # Use SECP256K1 curve for key generation (same as Bitcoin)
    pk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.curves.SECP256k1)
    public_key = pk.get_verifying_key().to_string(encoding="compressed")

    # Generate the address with prefix 0x38 ('P' address prefix)
    address = doublehash_base58_checksum(b'\x38' + hash160(public_key))

    # Uncompressed public key for display
    uncompressed_pubkey = pk.get_verifying_key().to_string(encoding="uncompressed").hex()

    # Save wallet details to wallet.txt
    with open("wallet.txt", "w") as f:
        f.write(f"Private Key     : {private_key.hex()}\n")
        f.write(f"Private Key WIF : {wif}\n")
        f.write(f"Public Key      : {public_key.hex()}\n")
        f.write(f"Phicoin Address : {address}\n")
        f.write(f"Uncompressed Public Key : {uncompressed_pubkey}\n")

    # Display the address in the GUI
    address_label.config(text=f"Address: {address}")
    messagebox.showinfo("Wallet Generated", "Wallet details saved to wallet.txt")

# Create the GUI window
window = tk.Tk()
window.title("Phicoin Wallet Generator")

# Input field to prompt the user for random input (optional use)
input_label = tk.Label(window, text="Enter some random characters for entropy:")
input_label.pack(pady=5)

user_input = tk.Entry(window, width=50)
user_input.pack(pady=5)

# Generate button
generate_button = tk.Button(window, text="Generate Wallet", command=generate_wallet)
generate_button.pack(pady=10)

# Label to display the generated address
address_label = tk.Label(window, text="Address: ", font=("Helvetica", 12))
address_label.pack(pady=10)

# Run the GUI event loop
window.mainloop()
