from Crypto.PublicKey import RSA

key = RSA.generate(2048)
public = key.publickey()


f = open('keys/private.pem','wb')
f.write(key.export_key('PEM'))
f.close()

f2 = open('keys/public.pem','wb')
f2.write(public.export_key('PEM'))
f2.close()