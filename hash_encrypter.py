import hashlib
from urllib.request import urlopen
from termcolor import colored


def hash_cracker(passwords):
    hash = input("[+] Enter the Hash value: \n")

    #checks the length of password hash and starts to compare hashes of the passwords from the url's password list.
    try:

        for password in passwords.split("\n"):
            if len(hash) == 32:
                guess = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
            if len(hash) == 40:
                guess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
            if len(hash) == 56:
                guess = hashlib.sha224(bytes(password, 'utf-8')).hexdigest()
            if len(hash) == 64:
                guess = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
            if len(hash) == 128:
                guess = hashlib.sha512(bytes(password, 'utf-8')).hexdigest()
            print(password)
            if guess == hash:
                print(colored("[+] The password is: " + str(password), 'green'))
                return True

            elif guess != hash:
                continue
            else:
                print(colored("The password didn't match in the list.. closing the program", 'red'))

    except Exception as exc:
        print("There was a problem: %s" % (exc))




def main():

    passwords = str(urlopen('https://raw.githubusercontent.com/danielmiessler/'
                            'SecLists/master/Passwords/Common-Credentials/10-million-'
                            'password-list-top-1000000.txt').read(), 'utf-8')
    hash_cracker(passwords)

    if hash_cracker(passwords) is not True:
        finnish_passwords = open("files/finnish_passwords.txt", "r")
        hash_cracker(finnish_passwords)
if __name__ == "__main__":
    main()

