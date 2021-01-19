from hashlib import sha256

def hashConversion(text):
    #converting into hash value
    return sha256(text.encode("ascii")).hexdigest()
    
def mine(block,transactions,previousHash,prefixZeros,difficulty):
    nounce=difficulty
    text = str(block)+transactions+previousHash+str(nounce)
    
    return hashConversion(text)

if __name__ == "__main__":
    transactions='''
    john->prince->30
    levin->shawn->50
    '''
#previous hash value :  00003c5b1ea1348d3e910891f7154b2e66504fcf02cd7bf1972736ec1e35c2ae
    i=1
    loop=True
    while loop:
        hashValue=mine(6,transactions,'00003c5b1ea1348d3e910891f7154b2e66504fcf02cd7bf1972736ec1e35c2ae',4,i)
        if hashValue[0:4]=='0000':
            print(hashValue)
            loop=False
            print(f"finally found the hash, hash value is {hashValue}")
        i+=1







   
