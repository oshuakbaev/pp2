with open('/Users/olzhas/Documents/GitHub/pp2/lecture_5/task1/w3res.txt') as fh1, open('a_file.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        # line1 from w3res.txt, line2 from a_file.txt
        print(line1+line2)