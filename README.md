# Hybrid PQC-Secure-File-Sharing-System
A hybrid Post-Quantum Cryptography (PQC)-based secure file sharing system that uses a PQC-inspired key exchange mechanism for shared secret generation, AES-GCM for secure file encryption, and SHA-256 for integrity verification. The system is designed to support future integration of real PQC algorithms such as CRYSTALS-Kyber.

## Features

- PQC-inspired key exchange mechanism
- AES-GCM based secure file encryption and decryption
- SHA-256 based integrity verification
- Sender–Receiver modular architecture
- File-based secure key storage
- Logging support for operations
- Scalable design for future PQC integration

## Project Structure

- PQC-Secure-File-Sharing-System/
- │
- ├── sender.py
- ├── receiver.py
- ├── pqc_key_exchange.py
- ├── files/
- │   ├── sample.txt
- │   ├── encrypted_file.bin
- │   ├── decrypted_file.txt
- │   └── shared_key.bin
- ├── logs/
- └── venv312/

## How to Run

1. Activate virtual environment:
   venv312\Scripts\activate

2. Run sender:
   python sender.py

3. Run receiver:
   python receiver.py

## Security Approach

- PQC-inspired KEM used for shared key generation
- AES-GCM used for secure file encryption (confidentiality + integrity)
- SHA-256 used for additional integrity verification

## Future Work

- Integration of CRYSTALS-Kyber using liboqs
- Network-based file transfer
- GUI development
- Digital signatures and authentication
