import secrets
import scrypt


def generate_key(length):
    password = 'to be passed or guessed'
    salt = secrets.token_bytes(64)
    key = scrypt.hash(password, salt, N=2048, r=8, p=1, buflen=length)
    #print (len(key))
    return (key)

def key_gen(length):
    password_provided = input('give a password') # This is input in the form of a string
    password = password_provided.encode() # Convert to type bytes    
    salt=b'\x12\xd9\xdcI_\xb3\x8b\xf0c\xf9\t\xbe \xa1F\x1b'
    key = scrypt.hash(password, salt, N=2048, r=8, p=1, buflen=length)
    #print (len(key))
    return (key)
