import encrypt
import decrypt
import datetime
import msvcrt

while True:
    encrypted = encrypt.encrypt(raw_input("\n\n\nEnter message to encrypt -- "))
    print "\nEncrypted Message -- \n"
    print encrypted
    print "\nDecrypted Message -- \n"
    msg = decrypt.decrypt(encrypted, str(datetime.datetime.now()))
    print msg
    print "\n\n\nPress Enter to try once again or any other key to quit......"
    if ord(msvcrt.getch()) != 13:
        exit(0)
