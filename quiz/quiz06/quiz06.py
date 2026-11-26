#문제 1

for i in range(5) :
    for j in range(5) :
        if i > j :
            continue
        print('*',end='')
    print()    


# 문제 2




for i in range(5):
    print(' ' * (4-i) + '*' * (2*i+1))


for i in range(5):
    for j in range(4-i):
        print(' ', end='')

    for j in range(2*i+1):
        print('*', end='')

    print()

for i in range(5) :
    for j in range(4-i) :
        print(' ',end='')    
    for k in range(2*i+1) :
        print('*',end='')    
    print()
print()        

for i in range(4,-1,-1) :
    for j in range(i) :
        print(" ",end='')
    for k in range(9-2*i) :
        print('*',end="")
    print()
print()           


n = int(input('숫자를 입력하시오.'))
for i in range(n):
    print(' ' * ((n-1)-i) + '*' * (2*i+1))
print()


for i in range(n-1,-1,-1):
    print(' ' * ((n-1)-i) + '*' * (2*i+1))
print()


for i in range(n-1):
    print(' ' * ((n-1)-i) + '*' * (2*i+1))



for i in range(n-1,-1,-1):
    print(' ' * ((n-1)-i) + '*' * (2*i+1))
print()
