# Diffie-Hellman Key Exchange

p = int(input("Enter prime number p: "))
g = int(input("Enter primitive root g: "))

a = int(input("Enter private key of Alice: "))
b = int(input("Enter private key of Bob: "))

A = pow(g, a, p)
B = pow(g, b, p)

alice_key = pow(B, a, p)
bob_key = pow(A, b, p)

print("Alice public key:", A)
print("Bob public key:", B)
print("Alice shared key:", alice_key)
print("Bob shared key:", bob_key)

if alice_key == bob_key:
    print("Key exchange successful!")
else:
    print("Key exchange failed!")