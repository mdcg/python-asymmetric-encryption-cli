from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

from src.utils import extract_or_create_filename, read_file, save_file
from src import logger


def decrypt_data(filename_path, new_filename_path, private_key_path):
    with open(filename_path, "rb") as file_in:
        logger.info(f"Decrypting file {filename_path}...")
        private_key = RSA.import_key(read_file(private_key_path))
        enc_session_key, nonce, tag, ciphertext = [
            file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)
        ]

        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        decrypt_filename = extract_or_create_filename(
            new_filename_path, filename_path
        )
        save_file(decrypt_filename, data)
        logger.info("File successfully decrypted.")
