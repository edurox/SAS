from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

key = RSA.generate(1024, e=65537)
publicKey = key.publickey()

#Open the file you want to certificate, hash it with sha256. After that encrypt it with RSA. 

file = open('sylvanas.jpg', 'r')
fileData = file.read()
fileHash = SHA256.new(fileData).digest()
hashEncrypted = key.encrypt(fileHash, 32)
file.close()

#Open or create assigned file, and save inside it the encrypted hash from the RSA.

fileAssigned = open('assigned.txt', 'w')
fileAssigned.write(str(hashEncrypted))
fileAssigned.close()

#Open or create certfication file, this recive both n and e public keys with a \n splitting it.

fileCertification = open('certification.txt', 'w')
fileCertification.write(str(publicKey.n) + "\n" + str(publicKey.e))
fileCertification.close()
