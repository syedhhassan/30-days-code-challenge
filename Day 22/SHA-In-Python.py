import hashlib

str = 'Syed'

result = hashlib.sha256(str.encode())

print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())

print ("\r")

str = 'Syed'

result = hashlib.sha384(str.encode())

print("The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())

print ("\r")

str = 'Syed'

result = hashlib.sha224(str.encode())

print("The hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())

print ("\r")

str = 'Syed'

result = hashlib.sha512(str.encode())

print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())

print ("\r")

str = 'Syed'

result = hashlib.sha1(str.encode())

print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())
