# RSA Algorithm

p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = pow(e, -1, phi)

print("Public Key:", (e, n))
print("Private Key:", (d, n))

message = int(input("Enter a number to encrypt: "))

encrypted = pow(message, e, n)
print("Encrypted Message:", encrypted)

decrypted = pow(encrypted, d, n)
print("Decrypted Message:", decrypted)