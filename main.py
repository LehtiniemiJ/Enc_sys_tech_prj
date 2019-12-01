import Generate_key
import chose_file
import AES_work2
import s_des_work
import Blowfish_work

def MainMenu():
    file_to_crypt = chose_file.chose() #chose file which is to be decrypted or crypted
    print ('file is ',file_to_crypt)
    i = int(input ('Chose 0 to Encrypt \nor\n1 to Decrypt\n'))
    print (i)

    if (i == 0):
        Encrypt(file_to_crypt)#insert calls for functions here
    elif(i == 1):
        Decrypt(file_to_crypt)
    else:
        print('invalid returning to mainmenu')

def Decrypt(file_to_crypt):
    ans = input ('chose algorith which is being used for encryption\n1 for AES\n2 for Blowfish\n3 for Sdes\n')
    ans = int(ans)
    if (ans == 1):
        print('using AES')
        AES_work2.decrypt_file(file_to_crypt)
    elif (ans == 2):
        print('using Blowfish')
        Blowfish_work.decrypt(file_to_crypt)
    elif (ans == 3):
        print('using SDES')
        s_des_work.decrypt(file_to_crypt)
    else:
        print ('not valid returning to mainmenu')
        MainMenu()
     
def Encrypt(file_to_crypt):
    ans = input ('chose algorith which is being used for decryption\n1 for AES\n2 for Blowfish\n3 for Sdes\n')
    ans = int(ans)
    
    if (ans == 1):
        print('using AES')
        iv = Generate_key.generate_key(16)
        AES_work2.encrypt_file(file_to_crypt,iv)
    elif (ans == 2):
        print('using Blowfish')
        iv = Generate_key.generate_key(8)
        Blowfish_work.encrypt(file_to_crypt,iv)
    elif (ans == 3):
        print('using SDES')
        iv = Generate_key.generate_key(8)
        s_des_work.encrypt(file_to_crypt,iv)
    else:
        print ('not valid returning to mainmenu')
        MainMenu()
       
MainMenu()


