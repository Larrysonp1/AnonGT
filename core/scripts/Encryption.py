import os
import shutil
import hashlib
import base64
import getpass
import zipfile
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


# ========================= KEY DERIVATION FUNCTION =========================
def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES requires 16, 24, or 32 bytes
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())


# ========================= AES ENCRYPTION =========================
def encrypt_file_aes(file_path, password):
    buffer_size = 64 * 1024
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(file_path, "rb") as f_in:
        with open(file_path + ".AnonGT", "wb") as f_out:
            f_out.write(salt + iv)
            while chunk := f_in.read(buffer_size):
                padding_length = 16 - (len(chunk) % 16)
                chunk += bytes([padding_length]) * padding_length  # PKCS7 Padding
                f_out.write(encryptor.update(chunk))
            f_out.write(encryptor.finalize())


# ========================= AES DECRYPTION =========================
def decrypt_file_aes(file_path, password):
    buffer_size = 64 * 1024
    with open(file_path, "rb") as f_in:
        salt = f_in.read(16)
        iv = f_in.read(16)
        key = derive_key(password, salt)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        output_file = file_path.replace(".AnonGT", "")

        with open(output_file, "wb") as f_out:
            while chunk := f_in.read(buffer_size):
                decrypted_chunk = decryptor.update(chunk)
                f_out.write(decrypted_chunk)
            f_out.write(decryptor.finalize())

        # Remove PKCS7 padding
        with open(output_file, "rb+") as f_out:
            data = f_out.read()
            padding_length = data[-1]
            f_out.seek(0)
            f_out.write(data[:-padding_length])
            f_out.truncate()


# ========================= FOLDER ENCRYPTION =========================
def encrypt_folder_aes(folder_path, password):
    zip_path = folder_path + ".zip"
    shutil.make_archive(folder_path, 'zip', folder_path)
    encrypt_file_aes(zip_path, password)
    os.remove(zip_path)

def decrypt_folder_aes(file_path, password):
    decrypt_file_aes(file_path, password)
    zip_path = file_path.replace(".AnonGT", "")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(zip_path.replace(".zip", ""))
    os.remove(zip_path)


