# RSA Program - Educational

import math

p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

n = p * q
phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    e += 1

d = pow(e, -1, phi)

print("Public Key  =", (e, n))
print("Private Key =", (d, n))

message = int(input("Enter message (number): "))

encrypted = pow(message, e, n)
decrypted = pow(encrypted, d, n)

print("Encrypted message =", encrypted)
print("Decrypted message =", decrypted)