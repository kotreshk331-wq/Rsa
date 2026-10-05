# AES Encryption/Decryption Program
# Install first: pip install cryptography

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

print("AES-style Symmetric Encryption Demo")
print("Key:", key.decode())

message = input("Enter message: ")

encrypted = cipher.encrypt(message.encode())
print("Encrypted:", encrypted.decode())

decrypted = cipher.decrypt(encrypted)
print("Decrypted:", decrypted.decode())