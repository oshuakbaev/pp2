"""
import re 

regex_pattern = r'[,.]'
a = re.split(regex_pattern,input())

for i in range(len(a)):
    print(a[i])
"""

regex_pattern = r"[.,]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))