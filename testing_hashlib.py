import hashlib
from urllib.request import urlopen
from termcolor import colored

hashValue = input("Enter a string to hash: \n")

hash_obj_1 = hashlib.md5()
hash_obj_1.update(hashValue.encode())
print("md5: ", hash_obj_1.hexdigest())
print("md5 block size: ", hash_obj_1.block_size)
print("md5 digest size: ", hash_obj_1.digest_size)
print("md5 length " + str(len(hash_obj_1.hexdigest())))

hash_obj_2 = hashlib.sha1()
hash_obj_2.update(hashValue.encode())
print("sha1: ", hash_obj_2.hexdigest())
print("sha1 block size: ", hash_obj_2.block_size)
print("sha1 digest size: ", hash_obj_2.digest_size)
print("sha1 length " + str(len(hash_obj_2.hexdigest())))

hash_obj_4 = hashlib.sha224()
hash_obj_4.update(hashValue.encode())
print("Sha224: ", hash_obj_4.hexdigest())
print("Sha224 Digest size ", hash_obj_4.digest_size)
print("sha224 length " + str(len(hash_obj_4.hexdigest())))


hash_obj_3 = hashlib.sha256()
hash_obj_3.update(hashValue.encode())
print("Sha256: ", hash_obj_3.hexdigest())
print("Sha256 digest size: ", hash_obj_3.digest_size)
print("sha256 length " + str(len(hash_obj_3.hexdigest())))




hash_obj_5 = hashlib.sha512()
hash_obj_5.update(hashValue.encode())
print("sha512:", hash_obj_5.hexdigest())
print("sha512 digest size:", hash_obj_5.digest_size)
print("sha512 length " + str(len(hash_obj_5.hexdigest())))