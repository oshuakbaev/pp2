import re

string = input()
    
match = re.search(r'([a-zA-Z0-9])\1+', string)

print(match.group(1) if match else -1)
