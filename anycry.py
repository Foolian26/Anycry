from pystyle import *
import ctypes
import base64
import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import time

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

def select():
    System.Init()
    System.Clear()
    System.Title("Anycry ꟾ 1.0 ꟾ \x46\x6F\x6F\x6C\x69\x61\x6E\x23\x36\x39\x38\x38")
    System.Size(100, 40)
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

def main2():
    System.Clear()
    print(Colorate.Format(Center.XCenter(logo), whiteChars, Colorate.Horizontal, Colors.red_to_white, Col.blue))
    rgb("Enter the file to be decrypted >>>")
    file_name = input('')
    if os.path.isfile(file_name):
        pass
    else:
        error("File does not exist")
        main2()
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

def main1():
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

if __name__ == '__main__':
    select()
