import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

key = RSA.generate(1024, Random.new().read) #Randomly generate a fresh, new RSA key object. Public and private keys (other person's)

publicKey = key.publickey() # PUBLIC KEY <<

#use his public key to encrypt your message

msg = publicKey.encrypt('ULTRA SECRET MSG. FOR NO ONE CAN FIND' \
                        'OUT WHAT IS GOING ON IM GOING TO ENCRYPT' \
                        'IT TO MAKE SURE THAT NO ONE WILL BE READING THIS', 32) #The message you wish to share with the other person

print '\nThis spam is your encrypted msg with the public key:\n\n', msg


#The other person can decrypt your message, since you used his public key to encrypt it

print '\nThe secret MSG:\n', key.decrypt(msg) #use the private key to decrypt the msg

