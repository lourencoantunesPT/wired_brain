#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
#EcbMode | CbcMode | CfbMode | OfbMode | CtrMode | OpenPgpMode | CcmMode | EaxMode | GcmMode | SivMode | OcbMode

from Crypto.Util.Padding import pad, unpad

data = b'secret data is bigger now because i invented some more text.'
data = b'ola'
key = get_random_bytes(16)

print('\n\n\n')
print('--- AES - CBC mode ---------')
print('\n')

print('---chave: ---')
print(key)
print('----------- ---')

cipher = AES.new(key, AES.MODE_CBC)
cipher_text = cipher.encrypt(pad(data, AES.block_size))
IV = cipher.IV

print('---plaintext inicial: ---')
print(data)
print('---ciphertext: ---')
print(cipher_text)
print('---IV: ---')
print(IV)

decrypt_cipher = AES.new(key, AES.MODE_CBC, IV)
plain_text = decrypt_cipher.decrypt(cipher_text)

print('---ciphertext: ---')
print(cipher_text)
print('---plain_text depois de decrypt(encrypt(): ---')
print(plain_text)


