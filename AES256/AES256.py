#Eduardo M Senger


from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto import Random

key_size = 32 #= aes256

iterations = 100


IV = Random.new().read(AES.block_size) #Inicializa o IV

salt = Random.new().read(key_size) #salt the hash

pkey = 'chave extremamente grande pq sim'

dkey = PBKDF2(pkey, salt, key_size, iterations)


cipher = AES.new(dkey, AES.MODE_CFB, IV)

textToCipher = cipher.encrypt('IM BATMAN')


dcipher = AES.new(dkey, AES.MODE_CFB, IV)

dcpt = dcipher.decrypt(textToCipher)

print(dcpt)
