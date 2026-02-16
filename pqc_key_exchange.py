import os
import hashlib

def generate_shared_secret():
    # simulate PQC shared secret using secure randomness
    return hashlib.sha256(os.urandom(32)).digest()
