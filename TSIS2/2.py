command = input('')
answer = ""
t2 = ""

dict = {"G":"G","()":"o","(al)":"al"}

for x in range(len(command)):
    t2 += command[x]
    if t2 in dict:
        answer += dict[t2]
        t2 = ""

    
print(answer)

