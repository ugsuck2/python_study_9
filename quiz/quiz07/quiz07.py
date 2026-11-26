import random
n = random.randint(1,100)
count = 0
while True :
    user = int(input('숫자를 입력하세요 :'))

    if count==7 :
        print(n,'까비요 기회끝')
        break

    if user>100 or user<1 :
        print('정확한 범위로 입력하세요')
        continue

    
    if user > n :
        print('down')
        count += 1
    elif user < n :
        print('up')
        count += 1
        
    else :
        print(user)
        print(count+1,'번')        