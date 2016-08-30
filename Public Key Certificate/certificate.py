from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

file = open('sylvanas.jpg', 'r')
fileData = file.read()
fileHash = SHA256.new(fileData).digest()
file.close()

fileAssigned = open('assigned.txt', 'r')
assignHash = fileAssigned.read()
fileAssigned.close()

certification = open('certification.txt', 'r')
publicKey = certification.read().splitlines()
n, e = int(publicKey[0]), int(publicKey[1])
certification.close()

key = RSA.construct((int(n), long(e)))
fileEncryptedHash = key.encrypt(fileHash, 32)

if str(fileEncryptedHash) == str(assignHash):
    print "\n \n \nIt's a valid certificate =D \n \n \n"
else:
    print "\n \n \nIt's a invalid certificate :( \n \n \n"
