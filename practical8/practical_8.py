from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import hashlib
import os

# Enter message
message = input("Enter your message: ")

# Generate AES key
key = AESGCM.generate_key(bit_length=256)
aes = AESGCM(key)

# Generate random nonce
nonce = os.urandom(12)

# Encrypt message
encrypted = aes.encrypt(nonce, message.encode(), None)

print("\nEncrypted Message:", encrypted.hex())

# Generate SHA-256 hash
hash_value = hashlib.sha256(message.encode()).hexdigest()

print("SHA-256 Hash:", hash_value)

# Decrypt message
decrypted = aes.decrypt(nonce, encrypted, None).decode()

print("Decrypted Message:", decrypted)

# Verify hash
new_hash = hashlib.sha256(decrypted.encode()).hexdigest()

if hash_value == new_hash:
    print("Message Integrity Verified!")
else:
    print("Message Integrity Failed!")