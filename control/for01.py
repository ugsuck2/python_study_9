
# for 반복문 range 0~4

# for 변수 in range() :

for i in range(5): # 0 1 2 3 4 
    print(i)

for i in range(3,10):
    print(i, end=" ")    
print()
for i in range(0,20,2):
    print(i, end=" ")        
print()

for i in range(10,0,-1):
    print(i, end=" ")        
print()

for i in reversed(range(0,10)) :
    print( i ,  end=' ')
print()    

# 입력 활욜
# count = int(input('횟수 입력 :'))
# for i in range(count):
#     print(i,end=' ')
# print()    

# 합계 1~100 
sum = 0
for i in range(1,101) :
    sum = sum + i
print('총합 :',sum)    

# 반복문 사용. 구조 자료형으로 사용 가능 : 리스트 튜플 문자열 시퀀스

fruits = ['사과','바나나','딸기','무화과']
for fruit in fruits:
    print(fruit)

for ch in 'Python' :
    print(ch, end=' ')
print()    

for i in range(len(fruits)):
    print(i, fruits[i])

for idx, item in enumerate(fruits) : # 인덱스, 값을 쌍으로 돌려준다
    print(idx,item)    

for i in range(1,10) :
    print(f'2 X {i} = {2*i}')  

# 안쓰는 값  _
for _ in range(10):
    print('*',end="")

print()          
