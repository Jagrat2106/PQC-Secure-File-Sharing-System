import hashlib
from pqc_key_exchange import load_shared_secret
from crypto_utils import decrypt_file

print("=== RECEIVER MODULE ===")

# Step 1: Generate same shared key (simulation)
shared_key = load_shared_secret()
aes_key = shared_key[:32]

print("Secure key received using PQC module")

# Step 2: Read encrypted file
with open("files/encrypted.bin", "rb") as f:
    nonce = f.read(16)
    tag = f.read(16)
    ciphertext = f.read()

# Step 3: Decrypt file
decrypted_data = decrypt_file(nonce, tag, ciphertext, aes_key)

# Step 4: Save decrypted file
with open("files/decrypted.txt", "wb") as f:
    f.write(decrypted_data)

# Step 5: Generate hash of decrypted file
decrypted_hash = hashlib.sha256(decrypted_data).hexdigest()

# Step 6: Read original hash
with open("files/hash.txt", "r") as f:
    original_hash = f.read().strip()

print("Original File Hash :", original_hash)
print("Decrypted File Hash:", decrypted_hash)

# Step 7: Verify integrity
if original_hash == decrypted_hash:
    print("Integrity verified: file is authentic")
else:
    print("Integrity check failed: file may be modified")

# Step 8: Logging
with open("logs/log.txt", "a") as log:
    log.write("File received, decrypted, and verified\n")

print("File decrypted and saved in files/decrypted.txt")
