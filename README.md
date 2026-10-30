# Cryptography Lab Practicals

This repository contains the 9 practicals I worked on for the Cryptography lab. The experiments cover classical ciphers, modern encryption, key exchange, hashing, digital signatures, and certificates. I used Python in VS Code, OpenSSL, and CrypTool depending on the practical.

The main goal was to understand how these techniques work by trying them out, rather than just studying the theory.

## Tools Used

- **VS Code and Python** – for writing and running encryption and hashing programs.
- **OpenSSL** – for RSA keys, file encryption, digital signatures, and X.509 certificates.
- **CrypTool** – for studying classical ciphers and frequency analysis.
- **Python `cryptography` library** – for AES encryption where needed.

## Practical 1: Classical Ciphers

**Aim:** Implement Caesar, Vigenère, and Rail Fence ciphers to encrypt and decrypt `HELLO WORLD`.

I used the same message with three different methods to see how each cipher changes the text. Caesar shifts letters by a fixed number, Vigenère uses a keyword to apply different shifts, and Rail Fence rearranges letters in a zigzag pattern. I also checked whether decrypting the ciphertext gives back the original message.

**What I learned:** These methods are easy to understand and implement, but they are not secure enough for modern communication.

## Practical 2: Frequency Analysis Using CrypTool

**Aim:** Perform frequency analysis on classical ciphertext and study its weaknesses.

In CrypTool, I looked at how often different letters appear in encrypted text. Common letters and repeated patterns can give clues about the original message, especially when a substitution cipher is used. Short ciphertexts can be harder to analyze because there is less data.

**What I learned:** Hiding letters does not always hide the patterns of a language. Frequency analysis is one way attackers can use those patterns.

## Practical 3: DES and AES Encryption

**Aim:** Encrypt sample data using DES and AES and compare their security and performance.

I tested encryption and decryption using DES and AES. DES uses a 56-bit effective key and is now considered insecure because its key can be brute-forced. AES supports stronger key sizes of 128, 192, and 256 bits and is widely used today. Performance can vary depending on the implementation and hardware.

**What I learned:** Both are symmetric encryption algorithms, but AES is the better choice for modern applications.

## Practical 4: RSA File Encryption Using OpenSSL

**Aim:** Generate RSA keys and encrypt and decrypt a file using OpenSSL.

I generated an RSA private key and extracted its public key. Then I encrypted a small text file with the public key and decrypted it with the private key. I checked that the decrypted content matched the original file.

**Files used:** `private.pem`, `public.pem`, `message.txt`, `encrypted.bin`, and `decrypted.txt`.

**What I learned:** RSA uses different keys for encryption and decryption. It works for small data, while larger files are normally protected using hybrid encryption.

## Practical 5: SHA-256 and Digital Signatures

**Aim:** Generate a SHA-256 hash, sign a message, and verify its signature using OpenSSL.

First, I generated the SHA-256 hash of a text file. Next, I signed the file with an RSA private key and verified the signature with the public key. I also changed the message and tried verifying it again. Verification failed after the change.

**Files used:** `message.txt`, `private.pem`, `public.pem`, and `signature.bin`.

**What I learned:** Hashes help detect changes, while digital signatures also connect a message to the signing key. The public key still needs to be trusted to confirm who signed it.

## Practical 6: Self-Signed X.509 Certificate

**Aim:** Create a self-signed X.509 certificate and examine its details.

Using OpenSSL, I generated a private key and created a certificate. I viewed information such as the subject, issuer, public key, signature algorithm, and validity dates. I also checked the certificate using OpenSSL's verification command.

**Files used:** `private.key` and `certificate.crt`.

**What I learned:** Certificates connect public keys with identities. A self-signed certificate can be useful for testing, but it is not automatically trusted by browsers or other systems.

## Practical 7: RSA and Diffie–Hellman in Python

**Aim:** Implement RSA and Diffie–Hellman to understand public-key cryptography and key exchange.

I wrote simple Python programs for both algorithms. The RSA program encrypted and decrypted a number using public and private keys. In Diffie–Hellman, two users calculated the same shared secret using their own private values and exchanged public values.

**What I learned:** RSA can be used for public-key encryption, while Diffie–Hellman is used to agree on a shared secret. The small numbers in these programs are only for learning.

## Practical 8: AES and SHA-256 for Text Messages

**Aim:** Build a Python program to encrypt text with AES and generate its SHA-256 hash.

I entered a text message, encrypted it using AES-GCM, and then decrypted it to get the original message back. I also generated a SHA-256 hash and compared it with the hash of the decrypted text.

**What I learned:** Encryption protects the contents of a message, while hashing produces a fingerprint of the data. AES-GCM also checks whether the encrypted data has been tampered with.

## Practical 9: Password Hashing With and Without Salt

**Aim:** Compare password hashes with and without salting and test them against common password guesses.

I hashed a password using SHA-256, then hashed it again after adding a random salt. I tested a small list of common passwords against both hashes. The salt changed the stored hash, but a weak password could still be guessed when the salt was known.

**What I learned:** Salting helps prevent the reuse of precomputed hashes and makes identical passwords produce different hashes. For real applications, password-specific methods such as Argon2id, scrypt, or bcrypt are safer than plain SHA-256.

## How to Run the Practicals

1. Open the relevant practical folder in VS Code or the required tool.
2. For Python programs, run `python filename.py` in the terminal.
3. For the AES practical, install the dependency using `pip install cryptography` if needed.
4. For OpenSSL practicals, run the commands in a terminal where `openssl` is installed and available.
5. For frequency analysis, open the experiment in CrypTool.

The exact filenames and commands may differ between practical folders. The RSA, Diffie–Hellman, and other classroom examples are for demonstration, not production security.

## Conclusion

These practicals helped me understand the difference between encryption, hashing, digital signatures, and key exchange. I also saw why older ciphers and weak passwords can be attacked, and why modern systems need stronger algorithms and proper key handling.
