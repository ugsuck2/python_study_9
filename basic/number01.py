# 숫자 정수형(int) 실수형 (float) 연산자

# 사칙연산

print(1+1)
print(5-3)
print(7*9)
print(7/2)  # 3.5
print(4/2)  # 2.0


# 몫 나머지
print(7//2) # 나눗셈 몫 -> 3
print(7%2)  # 나머지    -> 1

print(divmod(7,2))  # (3,1) (몫,나머지)

# 거듭제곱
print(2**5) #2의 5제곱

# 자료형 확인 : type()
print( type(10))
print( type(3.5))
print( type(4/2))


print(type(4//2))


# 정수 <-> 실수 변환
print(int(3.5)) # 정수형으로 변환 소수점 아래 버림
print(float(5)) # 실수형으로 변환
#print('100'+1) 파이썬은 문자형+숫자형 계산안됨
print(int('100')+1)

print('100'+str(1)) # str 문자열 형태로 변환

#실수 계산
print(0.1+0.2)
print((0.1+0.2)==0.3 )  #false

print(round(0.1+0.2,2))  #round 반올림 함수

# 계산 우선 순위

print(3+2*5)
print((3+2)*5)

# 숫자 표기, 큰 수 계산

print(12345567765*156498)
print(1,000,000)
print(1_000_000) # 숫자 가독성 측면으로 사용하는 구분자