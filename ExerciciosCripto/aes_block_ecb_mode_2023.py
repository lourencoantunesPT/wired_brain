#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
#EcbMode | CbcMode | CfbMode | OfbMode | CtrMode | OpenPgpMode | CcmMode | EaxMode | GcmMode | SivMode | OcbMode


data = b'\0'*32

key = get_random_bytes(16)

print('--- AES - ECB mode ---------')
print('\n')

print('---chave: ---')
print(key)
print('----------- ---')

cipher = AES.new(key, AES.MODE_ECB)
cipher_text = cipher.encrypt((data))


print('---plaintext inicial: ---')
print(data)
print('---ciphertext: ---')
print(cipher_text)

decrypt_cipher = AES.new(key, AES.MODE_ECB)
plain_text = decrypt_cipher.decrypt(cipher_text)

print('\n\n\n')
print('---ciphertext: ---')
print(cipher_text)
print('---plain_text depois de decrypt(encrypt(): ---')
print(plain_text)


