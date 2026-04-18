import os
import hashlib

KEY_PATH = "files/shared_key.bin"

def generate_shared_secret():
    # generate random key (PQC-like)
    random_bytes = os.urandom(32)
    shared_secret = hashlib.sha256(random_bytes).digest()

    # save key to file
    with open(KEY_PATH, "wb") as f:
        f.write(shared_secret)

    return shared_secret


def load_shared_secret():
    # load key from file
    with open(KEY_PATH, "rb") as f:
        return f.read()
