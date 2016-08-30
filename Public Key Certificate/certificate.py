from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

#Select file, read and then hash it with sha256

file = open('sylvanas.jpg', 'r')
fileData = file.read()
fileHash = SHA256.new(fileData).digest()
file.close()

#read the assigned file.

fileAssigned = open('assigned.txt', 'r')
assignHash = fileAssigned.read()
fileAssigned.close()

#open certification file, and read to n and e both the publickeys generated on main.py

certification = open('certification.txt', 'r')
publicKey = certification.read().splitlines()
n, e = int(publicKey[0]), int(publicKey[1])
certification.close()

#construct publickey and encrypt our sha256 encrypted file. 

key = RSA.construct((int(n), long(e)))
fileEncryptedHash = key.encrypt(fileHash, 32)

#if both private key encrypt and public key encrypted files are equals you have a valid certificate.

if str(fileEncryptedHash) == str(assignHash):
    print "\n \n \nIt's a valid certificate =D \n \n \n"
else:
    print "\n \n \nIt's a invalid certificate :( \n \n \n"
