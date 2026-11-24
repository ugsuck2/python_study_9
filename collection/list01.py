
# 리스트와 튜플

# 리스트(list) : 대괄호 [] 여러값 묶어서 저장

a = [12,34,56,78]
print(a)
print(type(a)) # <class 'list'>

# 자료형 상관없이 함께 저장  가능
person = ['홍길동',25,2863.5,True]
print(person)

# 빈리스트
b = []
c = list()
print(b,c)

#range() 활용 리스트 만들기

print( list(range(5,12)) ) 
print( list(range(0,20,2)) )
print( list(range(10,0,-1)) )

# 튜플 : 소괄호() 묶어서 값을 저장, 생성 후 값 변경 불가 const와 유사

t = (11,22,33,44)
print(t)
print(type(t))      #  <class 'tuple'>

t2 = 11,22,33 # 튜플로 저장됨
print(t2)

t3 = (38) # 정수로 인식

print(t3)

t4 = (36,) # 튜플로 인식
print(t4)

print(a[1])
print(t[2])
a[1] = 99
print(a[1])
#t[2] = 456 튜플은 생성 후 값변경 불가능 오류난다.

# a : list  t : tuple
# list tuple 변환
print( tuple(a))
print(list(t))

print(list('hello'))  # 문자열 분해해서 한글자씩 리스트로

x,y,z = [10,20,30]
q,w=(4,5)

print(x,y,z,q,w)