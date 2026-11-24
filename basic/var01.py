# 변수


# 변수명 = 값
x = 10
y = 3.14
name = '유광석'
is_ok = True   # 파이썬은 $ 안된다

print(x)
print(y)
print(name)
print(is_ok)

print(type(x),type(y),type(name),type(is_ok))


# 변수명

# 영문, 숫자, _ 특수문자 가능 / 숫자시작 불가
# 대소문자 구분(Name, name 다른변수)
# 키워드 사용불가 (if for class)
# 변수명은 의미있는 단어로 표현

# 자바,JS ---> 변수명 짓는 스타일 -> 카멜케이스 -> userName
# python ----> user_name

user_name = '파이썬'
print(user_name)
userName = '파이썬'

# 숫자형 n  --> n=20 n=10 n='문자'

# 변수에 값을 다시 저장하고 사용시 자료형이 바뀌어도 됨

x = 20
print(x,type(x))
x='문자열 저장'
print(x,type(x))

# 여러변수 동시에 저장
a,b,c = 10,20,30
print(a,b,c)
d=e=f=9
print(d,e,f)

# 두 변수의 값 바꾸기

print(a,b)
a,b = b,a
print(a,b)

# 변수삭제
del d
#print(d)  NameError: name 'd' is not defined

# 빈 변수 : None
z = None
print(z)

# 변수 계산
a = 10
b = 20
c = a + b
print(c)
c = a + a + b + b
print(c)

a = a + 5
a += 5
a -= 3
a *= 2
a //= 5
print(a)

x = -10
print(-x)