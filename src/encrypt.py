import os

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

from src.utils import read_file


def encrypt_data(filename_path, public_key_path):
    data = read_file(filename_path)
    encrypted_filename = f"{os.path.basename(filename_path).split('.')[0]}.bin"
    with open(encrypted_filename, "wb") as file_out:
        recipient_key = RSA.import_key(read_file(public_key_path))
        session_key = get_random_bytes(16)

        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)

        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        [
            file_out.write(x)
            for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)
        ]
