from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack
import Generate_key as new_generate_key

bs=Blowfish.block_size

def encrypt(filepath,iv):
        key = new_generate_key.key_gen(56)
        #print(len(key))
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
        with open(filepath,'rb') as fin:
	        with open('enc.blowf','wb') as fout:
                    data = fin.read()
                    plen = bs - len(data) % bs
                    padding = [plen]*plen
                    padding = pack('b'*plen, *padding)
                    encd = iv + cipher.encrypt(data+padding)
                    fout.write(encd)

def decrypt(filepath):
	with open(filepath,'rb') as fin:
            with open ('dec.blowf','w') as fout:
                key = new_generate_key.key_gen(56)
                data = fin.read()
                iv = data[:bs]
                #print ('iv is: ',iv)
                cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
                ciphtxt = data[bs:]
                decd = cipher.decrypt(ciphtxt).decode()
                fout.write(decd)

#encrypt(key,'file.txt',iv)
#decrypt(key,'enc.blowf')
