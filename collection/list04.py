# 리스트 중첩
# 2차원 리스트

# 2차원 행, 열
a = [ 
        [10,20] , 
        [30,40] , 
        [50,60] , 
        [70,80]
    ]

print(a)

print(a[1][1])

b = [ 
        [10,20] , 
        [30,40] , 
        [50,60] , 
        [70,80]
    ]

# 반복문으로 2차원 리스트 출력

for i in range(len(b)) :
    for j in range(len(b[i])):
        print(b[i][j],end=' ')
    print()  
print('-'*50)        

for row in b :
    for v in row :
        print(v, end=' ')
    print()    
print('-'*50)    

for x,y in b :
    print(x,y)   # x,y = [ 10 , 20 ]
print('-'*50)        


# 이차원 리스트 생성

# [ [], [], []   ]

c = []
for i in range(3) :
    temp = []
    for j in range(2) :    # []
        temp.append(j)
    # temp = [0,1]
    c.append(temp)
print(c)    
print('-'*50) 

d = [i for i in range(3)]
print(d)

e = [[j for j in range(2)] for i in range(3)]
print(e)

f =  [ [0]*5 for i in range(3)]
print(f)

# 학생          이름   학점 나이
students = [ ['john','c',19], ['maria','A',25], ['andrew','B',7]]
print(sorted(students))
print(sorted(students,reverse=True))
# 특정 위치의 열을 기준으로 정렬
print(sorted(students, key=lambda s: s[1]))
# lambda 한줄로 간단하게 작성하는 함수
print(sorted(students, key=lambda s: s[2],reverse=True))

# 2차원 리스트 복사
a = [[10,20],[30,40]]
b = a
print(a)
print(b)
a[0][0] = 90
print(a,b)
print('-'*50)

a = [[10,20],[30,40]]
b = a.copy()
a[0][0] = 90
print(a,b)
print('-'*50)

import copy
a = [[10,20],[30,40]]
b = copy.deepcopy(a)    # 주소의 주소까지 복사
a[0][0] = 90
print(a,b)
print('-'*50)


