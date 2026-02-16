from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from pqc_key_exchange import generate_shared_secret

# STEP 1: Generate secure shared key (simulated PQC)
shared_key = generate_shared_secret()

# AES requires 16/24/32 byte key → use first 32 bytes
aes_key = shared_key[:32]

print("Secure shared key established using PQC module")

# STEP 2: Read file
with open("sample.txt", "rb") as f:
    data = f.read()

# STEP 3: Encrypt file
cipher = AES.new(aes_key, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(data)

with open("encrypted_file.bin", "wb") as f:
    f.write(cipher.nonce + tag + ciphertext)

print("File encrypted successfully")

# STEP 4: Decrypt file
with open("encrypted_file.bin", "rb") as f:
    nonce = f.read(16)
    tag = f.read(16)
    ciphertext = f.read()

cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)

with open("decrypted_file.txt", "wb") as f:
    f.write(decrypted_data)

print("File decrypted successfully")
