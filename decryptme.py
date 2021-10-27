import string
import random
from base64 import b64encode, b64decode

secret = '2Mk16RXlXbkZhYjFweFduQkZVbWQ1Y2pGTlNGcEthMHBKVVZOcFRVbEZWM1JLU1hwSE0wbGpXakJKTVVkU1JEbERSRDA5' # My encrypted message

secret_decoding = ['step1', 'step2', 'step3']

def step1(s):
	_step1 = string.maketrans("zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA","mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON")
	return string.translate(s, _step1)

def step2(s): return b64decode(s)

def step3(plaintext, shift=-4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = string.maketrans(loweralpha, shifted_string)
    return plaintext.translate(converted)

def decrypt_secret(secret_text):
    while True:
        si = 0
        print ("po while", si)
        try:
            si = int(secret_text[0])
            r = secret_decoding[si-1]
            print ("w try", si, r)
        except:
            print ("wyjscie")
            return secret_text
        secret_text = secret_text[1:]
        _secret_text = globals()[r](secret_text)
        secret_text = _secret_text



if __name__ == '__main__':
	print decrypt_secret(secret) 




