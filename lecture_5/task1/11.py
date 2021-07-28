def file_size(text):
    import os 
    stat_info = os.stat(text)
    return stat_info.st_size

print(file_size('/Users/olzhas/Documents/GitHub/pp2/lecture_5/task1/w3res.txt'))