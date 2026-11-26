# 중첩 반복문

#if 조건 :
#     if : 조건

for i in range(3) :
    for j in range (4) :
        print(i,j) 

print()

for i in range(3) :
    for j in range(4) :
        print (j)

print()

for i in range (5) :
    print('*'*i)
print()
for i in range (5) :
    print('*',end='')
    i += 1
    if i == 4 :
        break
print()

for i in range(5) :
    for j in range (5) :
        print('*', end="")
    print()
print()    

for i in range(3):
    print('*'*10)
print()


for i in range(5):
    for j in range(5):
        if j<=i:
            print('*',end='')
    print()
print()            

for i in range(5):
    print('*'*(i+1))
print()

for i in range(5):
    for j in range(5):
        if i == j:
            print('*',end='')
        else :
            print(' ',end='')
    print()
print()           

for i in range(5):
    for j in range(5):
        if j<4-i :
            print(' ',end='')
        else :
            print('*',end='')
    print()
print()    

for i in range(2,10) :
    print(i,'단')
    for j in range(1,10) :
        print(i,'X',j,'=',i*j)
    print('-'*20)