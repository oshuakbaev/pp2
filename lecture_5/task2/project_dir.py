import os 
import shutil
from typing import Counter
Counter_dir = 0 # -----> Counter of dir 

Files = 0 # -----> Counter of files 
os.chdir('/Users/olzhas/Documents/GitHub')
os.rename('test', 'test_changed') # - rename dir $

for obj in os.listdir('.'):  # -----> number of files $
    if os.path.isfile(obj):
        Files+=1


for obj in os.listdir('.'): 
    if os.path.isdir(obj):
        Counter_dir+=1        # -----> number of dir $
        print(f'Folder:{obj}\n') # -----> consisting of dir $
print(Counter_dir) # printing counter of dir $

for root, dirs, files in os.walk('.'): #consisting of dir $ 
  print(root)
  print(dirs)
  print('-'*70)

shutil.move('example.txt','Dr2') # -------> add to the dir $

""" add new file to the dir """ 
f = open('mv_dir.txt','x') 
shutil.move('mv_dir.txt','Dr2')   

#a = os.mkdir('Dr2')
#f = open('aba.txt','x')

os.mkdir('Dr3') # -------> creat a dir









