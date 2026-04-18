import hashlib
from pqc_key_exchange import generate_shared_secret
from crypto_utils import encrypt_file

print("=== SENDER MODULE ===")

# Step 1: Generate shared key
shared_key = generate_shared_secret()
aes_key = shared_key[:32]

print("Secure key generated using PQC module")

# Step 2: Take file input
filename = input("Enter file name to send: ")

with open(filename, "rb") as f:
    data = f.read()

# Step 3: Generate hash (for integrity)
original_hash = hashlib.sha256(data).hexdigest()
print("Original File Hash:", original_hash)

# Step 4: Encrypt file
nonce, tag, ciphertext = encrypt_file(data, aes_key)

# Step 5: Save encrypted file
with open("files/encrypted.bin", "wb") as f:
    f.write(nonce + tag + ciphertext)

# Step 6: Save hash (for verification later)
with open("files/hash.txt", "w") as f:
    f.write(original_hash)

# Step 7: Logging
with open("logs/log.txt", "a") as log:
    log.write("File encrypted and sent successfully\n")

print("File encrypted and stored in files/encrypted.bin")
