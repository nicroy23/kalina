from os import stat
from typing import Dict
from cryptography.fernet import Fernet, InvalidToken
import json
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import actions.all_entries as AE
import actions


# Global reference to all entries object
#entry_obj = None
#user_pwd = ""


class File:
    @staticmethod
    def create_file(pwd: str):
        #global user_pwd
        #user_pwd = pwd

        encoded_key = pwd.encode()
        salt = b'eyuihdbsjc78fdsa4676ghgsgfs'

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )

        new_key = base64.urlsafe_b64encode(kdf.derive(encoded_key))

        # Create the basestore. json for the file and write it
        # to the newly created file
        with open("pass.kalina", "w") as f:
            data = {}
            data["passwords"] = []
            json.dump(data, f)

        # Read the bytes from the file to encrypt it
        with open("pass.kalina", "rb") as f:
            file = f.read()

        # Encrypt the file with the password
        fernet = Fernet(new_key)
        encrypted = fernet.encrypt(file)

        # Re-write the encrypted data in the file
        with open("pass.kalina", "wb") as f:
            f.write(encrypted)

        actions.Store.passwords = []

    @staticmethod
    def save():
        encoded_key = actions.Store.user_pwd.encode()
        salt = b'eyuihdbsjc78fdsa4676ghgsgfs'

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )

        new_key = base64.urlsafe_b64encode(kdf.derive(encoded_key))

        with open("pass.kalina", "w") as f:
            json.dump(actions.Store.passwords, f)

        with open("pass.kalina", "rb") as f:
            file = f.read()

        fernet = Fernet(new_key)
        encrypted = fernet.encrypt(file)

        # Re-write the encrypted data in the file
        with open("pass.kalina", "wb") as f:
            f.write(encrypted)

    @staticmethod
    def read_file(pwd: str) -> Dict:
        """
        This function reads the encrypted file by decrypting it using
        the user's password. Then, it updates the object to include the
        data read and if the password was validated.
        """
        #global entry_obj
        #global user_pwd

        #user_pwd = pwd

        encoded_key = pwd.encode()
        salt = b'eyuihdbsjc78fdsa4676ghgsgfs'

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )

        new_key = base64.urlsafe_b64encode(kdf.derive(encoded_key))

        with open("pass.kalina", 'rb') as f:
            data = f.read()  # Read the bytes of the encrypted file

        fernet = Fernet(new_key)
        response = {
            "validated": False,
            "data": None
        }

        try:
            # Decrypt data and transform it in json
            decrypted = fernet.decrypt(data)
            decrypted = decrypted.decode("utf-8")
            decrypted_json = json.loads(decrypted)

            # Affect response object that communicates with gui
            # to know which window to open next
            response["validated"] = True
            response["data"] = decrypted_json

            # Since the password is validate, we create the object
            # that contains all the passwords and performs actions
            # on them
            #entry_obj = AE.AllPasswords(decrypted["passwords"])

            actions.Store.passwords = decrypted_json
            actions.Store.user_pwd = pwd

        except InvalidToken:
            print("Invalid Key - Unsuccessfully decrypted")

        return response

    # @staticmethod
    # def get_entry_obj():
    #     global entry_obj

    #     return entry_obj

    # @staticmethod
    # def get_user_pwd():
    #     global user_pwd

    #     return user_pwd
