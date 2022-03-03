from base64 import b32decode, decode
from codecs import utf_16_be_encode
from ctypes.wintypes import HLOCAL
from hashlib import md5

import hashlib


clave_secreta = hashlib.sha256(b'2232')
hash = clave_secreta.hexdigest()
hash2 = hashlib.md5(hash)

print(hash2)

#hash2 = hash.decode('utf-8')

#print(hash2)