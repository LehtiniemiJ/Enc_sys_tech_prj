from Crypto.Cipher import DES
import Generate_key as new_generate_key

def encrypt(filepath,iv):
	key = new_generate_key.key_gen(8)
	cipher = DES.new(key,DES.MODE_CBC, iv)
	with open(filepath,'rb') as fin:
		with open('enc.sdes','wb') as fout:
			data = fin.read()
			n = len(data)
			data += b' ' * (8 - n % 8)
			encd = iv + cipher.encrypt(data)
			fout.write(encd)

def decrypt(filepath):
	with open(filepath,'rb') as fin:
		with open ('dec.sdes','w') as fout:
			key = new_generate_key.key_gen(8)

			data = fin.read()
			iv = data[:8]
			#print ('iv is: ',iv)
			cipher = DES.new(key,DES.MODE_CBC, iv)
			ciphtxt = data[8:]
			decd = cipher.decrypt(ciphtxt).decode()
			fout.write(decd)
