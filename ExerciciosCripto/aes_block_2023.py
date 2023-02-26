#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from binascii import hexlify as hexa
from os import urandom


data = b'secret data is bigger now because i invented some more text.'
key = urandom(16)

print('--- AES - CTR mode ---------')
print('\n')

print('---chave: ---')
print(key)
print('----------- ---')

cipher = AES.new(key, AES.MODE_CTR)
cipher_text = cipher.encrypt(data)
nonce = cipher.nonce

print('---plaintext inicial: ---')
print(data)
print('---ciphertext: ---')
print(cipher_text)
print('---nonce: ---')
print(nonce)

decrypt_cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
plain_text = decrypt_cipher.decrypt(cipher_text)

print('\n\n\n')
print('---ciphertext: ---')
print(cipher_text)
print('---plain_text depois de decrypt(encrypt(): ---')
print(plain_text)


