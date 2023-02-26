#!/usr/bin/env python3

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from binascii import hexlify as hexa
from os import urandom


#pick a random 16-byte key using Python's crypto PRNG
k = urandom(16)
print("chave para o aes - k = ",hexa(k))

#create an instance of AES-128 to encrypt a single block
cipher = Cipher(algorithms.AES(k), modes.ECB())
aes_encrypt = cipher.encryptor()
type(aes_encrypt)

#set plaintext block p to the all-zero string
p = '\x00' * 16
#encrypt plaintext p to ciphertexst c
c = aes_encrypt.update()
aes_encrypt.finalize()

print("enc(%) = %",(hexa(p), hexa(c)))

#decrypt ciphertext to plaintext p
aes_decrypt = cipher.decryptor()
p2 = aes_decrypt.update(c)
aes_decrypt.finalize()

print("dec(%s) =%s ",(hexa(c), hexa(p2)))

