import hashlib
import os

password = input("Enter Password: ")

# 1. Hashing without salt
hash1 = hashlib.sha256(password.encode()).hexdigest()
print("\nHash Without Salt:", hash1)

# 2. Hashing with salt
salt = os.urandom(16)

hash2 = hashlib.sha256(salt + password.encode()).hexdigest()

print("\nSalt:", salt.hex())
print("Hash With Salt:", hash2)

# 3. Dictionary Attack Simulation
common_passwords = ["123456", "password", "admin", "hello123"]

print("\nDictionary Attack (Without Salt):")

found = False

for word in common_passwords:
    test_hash = hashlib.sha256(word.encode()).hexdigest()

    if test_hash == hash1:
        print("Password Cracked:", word)
        found = True
        break

if not found:
    print("Password Not Found")

# 4. Dictionary Attack With Salt
print("\nDictionary Attack (With Salt):")

found = False

for word in common_passwords:
    test_hash = hashlib.sha256(salt + word.encode()).hexdigest()

    if test_hash == hash2:
        print("Password Cracked:", word)
        found = True
        break

if not found:
    print("Password Not Found")