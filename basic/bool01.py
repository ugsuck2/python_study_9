
# bool 자료형
# True | False (첫글자 대문자로 써야됨)
print(True,False)
#print(true,false)
print(type(True))

# 비교연산자 -> 결과 True | False
print(10 == 10)
print(10 != 10)
print(10>20)
print(10<20)
print(10>=20)
print(10<=20)

# 문자열 비교
print('Python' == 'Python')
print('Python' == 'python')
print('Python' != 'Python')
print('Python' != 'python')

# 값 ==   객체 비교 is
n1 = 1
n2 = 1.0
print(n1==n2)
print(type(n1)==type(n2))

print(n1 is n2)
print(type(n1) is type(n2))

x = None

print( x == None)
print( x is None) # None 비교시에는 is를 사용


# 논리연산자 and or not

print(True and (1==1))
print(False or True)
print(not True)

age = 25
print( age>=20 and age < 30)
print( 20 <= age < 30) # 파이썬은 허용

print( age > 10 or age < 100)

# 정수, 실수, 문자열 -> bool

print(bool(1),bool(0))  # 숫자형은 0만 false

print(bool('a'),bool(' '),bool('')) #문자형은 빈 문자열이 false 

print(bool([]),bool([1,2,3])) # 리스트는 빈 리스트만 false

# && ||
print(False and 'abc')
print(True and 'abc')  # {True %% <요소>}
print(False or 'def')