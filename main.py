import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# ----------------------------
# STEP 1: Simulated PQC Key Exchange (Using RSA for demo)
# ----------------------------

def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

# ----------------------------
# STEP 2: Generate AES key
# ----------------------------

def generate_aes_key():
    return Fernet.generate_key()

# ----------------------------
# STEP 3: Encrypt AES key with public key
# ----------------------------

def encrypt_aes_key(aes_key, public_key):
    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_key

# ----------------------------
# STEP 4: Decrypt AES key
# ----------------------------

def decrypt_aes_key(encrypted_key, private_key):
    return private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

# ----------------------------
# STEP 5: Encrypt File
# ----------------------------

def encrypt_file(file_path, aes_key):
    cipher = Fernet(aes_key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    with open("encrypted_file.bin", "wb") as file:
        file.write(encrypted_data)

    print("File encrypted successfully!")

# ----------------------------
# STEP 6: Decrypt File
# ----------------------------

def decrypt_file(aes_key):
    cipher = Fernet(aes_key)

    with open("encrypted_file.bin", "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open("decrypted_file.txt", "wb") as file:
        file.write(decrypted_data)

    print("File decrypted successfully!")

# ----------------------------
# MAIN PROGRAM
# ----------------------------

if __name__ == "__main__":
    print("Generating Keys...")
    private_key, public_key = generate_keys()

    print("Generating AES Key...")
    aes_key = generate_aes_key()

    print("Encrypting AES key using Public Key...")
    encrypted_aes_key = encrypt_aes_key(aes_key, public_key)

    print("Decrypting AES key using Private Key...")
    decrypted_aes_key = decrypt_aes_key(encrypted_aes_key, private_key)

    encrypt_file("sample.txt", decrypted_aes_key)
    decrypt_file(decrypted_aes_key)

    print("Secure File Sharing Process Completed Successfully!")
