
# 큰따옴표, 작은따옴표 상관없다
hello = 'Hello, World'
hi = "안녕하세요"

print(hello)
print(hi)
print(type(hi))

s1 = "my name's ..."
s2 = 'hi"hello"'
s3 = '큰따옴표 작은\'\" 따옴표'
print(s1)
print(s2)
print(s3)

s4 = '''
여러줄
문자열을
나타낼때
사용도 가능
'''
print(s4)

'''
이것 사용을 
여러줄 주석처럼
사용도 가능

'''
s5 = """
여러줄
문자열을
나타낼때 "큰따옴표도 가능"
사용도 가능
"""
print(s5)

#이스케이프 문자
print('줄바꿈\n문자')
print('탭 띄어쓰기 \t 문자')
print('역슬래쉬\\ \\ 문자')

a = 'hello'
b = 'world'
print(a + b)
print(a + ' ' + b)
print(a,b,sep=" ")
print('-'*30)

# 문자 함수
print(len(a))
print(len('글자길이를 맞춰보세요.'))
print('ll'in a)
print('ll'in b)
print('ll'not in b)

num = '123'
print(int(num) + 123)
print(str(123)+'456')