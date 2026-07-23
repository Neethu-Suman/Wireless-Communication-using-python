import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
# Generate a random 256-bit key
key = os.urandom(32)
# Derive a key from the password
password = b"my_secret_password"
salt = b"my_secret_salt"
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256,
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))
# Create a Fernet object using the derived key
fernet = Fernet(key)
# Encrypt the plaintext
plaintext = b"This is my secret message"
ciphertext = fernet.encrypt(plaintext)
print(ciphertext)
# Decrypt the ciphertext
plaintext = fernet.decrypt(ciphertext)
print(plaintext)
