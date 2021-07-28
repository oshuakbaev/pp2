import re
from collections import Counter

def freq(text):
    with open(text,'r') as f: 
        res = re.findall('\w{1,}',f.read())
        count = Counter(res)
    return count 



print(freq("w3res.txt"))