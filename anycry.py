from pystyle import *
from sys import executable
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import ctypes
import base64
import os
import time
import subprocess

whiteChars = list('@')

logo = """


          :::     ::::    ::: :::   :::  ::::::::  :::::::::  :::   ::: 
       :+: :+:   :+:+:   :+: :+:   :+: :+:    :+: :+:    :+: :+:   :+:  
     +:+   +:+  :+:+:+  +:+  +:+ +:+  +:+        +:+    +:+  +:+ +:+    
   +#++:++#++: +#+ +:+ +#+   +#++:   +#+        +#++:++#:    +#++:      
  +#+     +#+ +#+  +#+#+#    +#+    +#+        +#+    +#+    +#+        
 #+#     #+# #+#   #+#+#    #+#    #+#    #+# #+#    #+#    #+#         
###     ### ###    ####    ###     ########  ###    ###    ###          

"""

menu ="""

[1] Encrypt

[2] Decrypt

"""
def pipinstaller():
    requirements = [
        ["pystyle"],
        ["Crypto.Cipher", "pycryptodome"]
    ]
    for modl in requirements:
        try:
            __import__(modl[0])
        except:
            subprocess.Popen(f"{executable} -m pip install {modl[1]}", shell=True)
            time.sleep(3)
def select():
    pipinstaller()
    System.Init()
    System.Clear()
    exec("\x53\x79\x73\x74\x65\x6D\x2E\x54\x69\x74\x6C\x65\x28\x22\x41\x6E\x79\x63\x72\x79\x20\x2D\x20\x31\x2E\x31\x20\x2D\x20\x46\x6F\x6F\x6C\x69\x61\x6E\x23\x36\x39\x38\x38\x22\x29")
    System.Size(100, 40)
    Anime.Fade(text=Center.Center(logo), color=Colors.red_to_white, mode=Colorate.Horizontal, enter=True)
    print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
    print(Colorate.Format(Center.XCenter(menu), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
    choice = input()
    if choice == "1":
        main1()
    elif choice == "2":
        main2()
    else:
        select()

def rgb(what):
    print(Colorate.Format(Center.XCenter(what), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))

def rgb2(what):
    print(Colorate.Horizontal(Colors.red_to_white, what, 1))

def error(message):
    ctypes.windll.user32.MessageBoxW(0, message, "Error", 0x00000010)

def encrypt(file_name, password):

    salt = os.urandom(8)

    key = PBKDF2(password, salt, dkLen=32)

    iv = os.urandom(16)

    cipher = AES.new(key, AES.MODE_CFB, iv)
    with open(file_name, 'rb') as f:
        file_data = f.read()
    encrypted_data = cipher.encrypt(file_data)

    with open(file_name + '.anycry', 'wb') as f:
        f.write(salt + iv + encrypted_data)

def encrypt_folder(folder, password):

    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt(file_path, password)
            os.remove(file_path)

def decrypt_file(file_name, password):
    try:

        with open(file_name, 'rb') as f:
            salt = f.read(8)
            iv = f.read(16)
            encrypted_data = f.read()

        key = PBKDF2(password, salt, dkLen=32)

        cipher = AES.new(key, AES.MODE_CFB, iv)
        decrypted_data = cipher.decrypt(encrypted_data)

        try:
            decrypted_str = decrypted_data.decode('utf-8')
        except UnicodeDecodeError:

            return False
        else:

            with open(file_name[:-7], 'wb') as f:
                f.write(decrypted_data)
            return True
    except ValueError:

        return False

def decrypt_file2(file_name, password):
    try:

        with open(file_name, 'rb') as f:
            salt = f.read(8)
            iv = f.read(16)
            encrypted_data = f.read()

        key = PBKDF2(password, salt, dkLen=32)

        cipher = AES.new(key, AES.MODE_CFB, iv)
        decrypted_data = cipher.decrypt(encrypted_data)

        with open(file_name[:-7], 'wb') as f:
            f.write(decrypted_data)
        return True

    except ValueError:

        return False

def decrypt_folder(folder, password):

    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            if decrypt_file(file_path, password):

                os.remove(file_path)


def main2():
    System.Clear()
    print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
    rgb("""

                [1] Decrypt File

                [2] Decrypt Folder

            """)
    cho = input("")

    if cho == "2":

        System.Clear()
        print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
        rgb("Enter the Folder to be decrypted >>>")
        folder_name = input('')
        if os.path.exists(folder_name):
            pass
        else:
            error("Folder does not exist")
            main2()
        System.Clear()
        print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
        rgb("""

                [1] Enter your own Password

                [2] Use your own Password File

            """)
        choice = input("")

        if choice == "1":
            System.Clear()
            print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
            rgb("Enter Password to decrypt >>> ")
            password3 = input()
            start = time.time()
            decrypt_folder(folder_name, password3)
            end = time.time()
            sec = start - end
            rgb(f"Folder decrypted successfully with password: {password3} in {sec}")

        elif choice == "2":
            """
            System.Clear()
            print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
            rgb("Enter Password File (Unformatted)")
            password_file = input()

            try:
                with open(password_file, "r") as a:
                    a.read()
            except:
                error("Password File does not exist")
                main2()
            num = 0
            with open(password_file, 'r') as f:
                for password in f:
                    password = password.strip()
                    num += 1
                    rgb2(f"Testing {password} Attempt: {num}")
                    if decrypt_folder(folder_name, password):
                        rgb(f"Folder decrypted successfully with password: {password}")
                        break
                else:
                    rgb(f"Could not decrypt folder with any of the given passwords.")
            """
            System.Clear()
            print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
            rgb("Coming Soon...")

        time.sleep(5)
        select()
    if cho == "1":
        System.Clear()
        print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
        rgb("Enter the file to be decrypted >>>")
        file_name = input('')
        if os.path.isfile(file_name):
            pass
        else:
            error("File does not exist")
            main2()

        System.Clear()
        print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
        rgb("""

                        [1] Enter your own Password

                        [2] Use your own Password File

                    """)
        choice = input("")

        if choice == "1":
            System.Clear()
            print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
            rgb("Enter Password to decrypt >>> ")
            password3 = input()
            if password3 == None:
                error("Do not enter a blank Password")
            else:
                if decrypt_file2(file_name, password3):

                    rgb(f"File decrypted successfully with password: {password3}")

                else:
                    rgb("Wrong Password")

        elif choice == "2":

            System.Clear()
            print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
            rgb("Enter Password File (Unformatted)")
            password_file = input()

            try:
                with open(password_file, "r") as a:
                    a.read()
            except:
                error("Password File does not exist")
                main2()
            num = 0
            with open(password_file, 'r') as f:
                for password in f:
                    password = password.strip()
                    num += 1
                    rgb2(f"Testing {password} Attempt: {num}")
                    if decrypt_file(file_name, password):
                        rgb(f"File decrypted successfully with password: {password}")
                        break
                else:
                    rgb(f"Could not decrypt file with any of the given passwords.")
        time.sleep(5)
        select()
    else:
        main2()


def main1():
    System.Clear()
    print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
    rgb("""
    
            [1] Encrypt File
            
            [2] Encrypt Folder
            
        """)
    cho = input("")
    if cho == "1":
        System.Clear()
        print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
        rgb("Enter the file to be encrypted >>> ")
        file = input()
        if os.path.isfile(file):
            pass
        else:
            error("File does not exist")
            main1()

        System.Clear()
        print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
        rgb("Enter the master password to be used for encryption >>> ")
        password = input()
        if password == "":
            error("Do not enter a blank password")
            main1()
        else:
            pass
        start = time.time()
        encrypt(file, password)
        end = time.time()
        total = end - start

        rgb(f"File encrypted successfully in {total}s")
        time.sleep(5)
        select()

    if cho == "2":
        System.Clear()
        print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
        rgb("Enter the Folder to be encrypted >>> ")
        folder = input()
        if os.path.exists(folder):
            pass
        else:
            error("Folder does not exist")
            main1()

        System.Clear()
        print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
        rgb("Enter the master password to be used for encryption >>> ")
        password = input()
        if password == "":
            error("Do not enter a blank password")
            main1()
        else:
            pass
        start = time.time()
        encrypt_folder(folder, password)
        end = time.time()
        total = end - start

        rgb(f"Folder encrypted successfully in {total}s")
        time.sleep(5)
        select()

    else:
        System.Clear()
        main1()


if __name__ == '__main__':
    select()
