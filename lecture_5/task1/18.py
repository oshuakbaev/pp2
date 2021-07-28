def count_words(filepath):
   with open(filepath) as f:
       data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("/Users/olzhas/Documents/GitHub/pp2/lecture_5/task1/w3res.txt"))