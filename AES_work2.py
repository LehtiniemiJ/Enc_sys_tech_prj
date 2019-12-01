from Crypto.Cipher import AES
import Generate_key as new_generate_key

sz = 2048


def encrypt_file(filepath,iv):
   # print ('iv :',iv)
    print ('filepath :',filepath)
    key = new_generate_key.key_gen(32) #should be 128,192,256 bits long (respectively for AES-128, AES-192 or AES-256).
    aes = AES.new(key, AES.MODE_CBC, iv)

    with open(filepath,'rb') as f:
        with open ('enc.aes','wb') as fout:
            while True:
                data = f.read(sz)
                n = len(data)
                if n == 0:
                    break
                elif n % 16 != 0:
                    data += b' ' * (16 - n % 16) # <- padded with spaces
                encd = iv+ aes.encrypt(data)
                fout.write(encd)

def decrypt_file(filepath):
    with open (filepath, 'rb+') as f:
        with open ('dec.aes','w') as fout:
            while True:
                key = new_generate_key.key_gen(32) #should be 128,192,256 bits long (respectively for AES-128, AES-192 or AES-256).
                data = f.read()
                iv = data[:16]
               # print(iv)
               # print(len(iv))
                data = data[16:]
                n = len(data)
                aes = AES.new(key, AES.MODE_CBC, iv)
                if n == 0:
                    break
                else:
                    #print('length',len(data))
                   # print(data)
                    decd = aes.decrypt(data).decode('utf-8')
                    #print (decd)
                    fout.write(decd)


#iv = os.urandom(16)  #generate iv

#encrypt_file('test.txt',b'\x92/\x8c\x90\x9f\x88r\xe3\x8069\x15\x91\xd8\xfb ')
#decrypt_file('enc.aes')
