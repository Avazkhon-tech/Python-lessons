n = 0
while True:
    info = input("do'stlaringiz ismini birma bir kiriting kiriting: ")
    if not info: break
    with open('dars-33-friends_list.txt','a') as file:
        n+=1
        file.write(f' {n}. {info}' '\n')
        
