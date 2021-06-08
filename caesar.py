alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
            'O','P','Q','R','S','T','U','V','W','X','Y','Z']


def encrypt(keys, words):
    
    lst = list(words.upper())
    
    idx = [alphabet.index(i) for i in lst]
    
    index = [keys - len(alphabet[i:]) for i in idx]
        
    sentence = ''.join(alphabet[i] for i in index)
    
    print(sentence.title())
        
    
    
def decrypt(keys, words):
    

    lst = list(words.upper())
    
    idx = [alphabet.index(i) for i in lst]
    
    
    for i in idx:
        print(i - keys)
    
    sentence = ''.join(alphabet[i - keys] for i in idx)
    
    print(sentence.title())
        
    
    
#encrypt(1, 'GIEWIVrGMTLIVrHIQS')

decrypt(25, 'GIEWIVRGMTLIVRHIQS')