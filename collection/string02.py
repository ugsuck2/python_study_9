

s = 'Hello, world!'

# 문자 바꾸기 (대체하기) replace(대상,바꿀값)

print( s.replace('world','Mike'))  # 원본 유지  비파괴적
print(s)

s = s.replace('world','Mike')
print(s)

# 분리 / split   join   ['','']
words = 'apple kiwi banana melon'.split()
print(words)
print('apple,kiwi,banana,melon'.split(','))

# 구분자.join(리스트)
print('-'.join(words))
print('/'.join(words))
print(''.join(words))

#대소문자
print('hello'.upper())
print('GREAT'.lower())
print('hello great'.title())   # 단어 앞글자 대문자
print('hello great'.capitalize())   # 첫글자 앞글자만 대문자

# 공백 제거 (입력값 정리)
text = '    womderful       '
print('[',text.strip(),']')
print('[',text.lstrip(),']')
print('[',text.rstrip(),']')

print('[',' .  this is text!!  '.strip('.! '),']') 
#양쪽 끝에있는 지정한 문자를 정리


# 문자열 폭 정렬 
print('[','python'.ljust(10),']')
print('[','python'.rjust(10),']')
print('[','python'.center(10),']')
print('[','python'.zfill(10),']')
print('2'.zfill(2))

print('[','python'.ljust(10,"*"),']')

# 문자 찾기
s = 'apple pineapple'
print(s.find('pl')) # 앞에서 부터 찾아서 가장 먼저 찾은 위치
print(s.rfind('pl')) # 오른쪽에서부터찾기
print(s.find('ex'))   # 없으면 -1
print(s.index('pl'))  # 찾은 인덱스 못찾으면 오류 발생
print(s.count('p')) # 갯수 세기

# 시작 끝 확인
file_name = 'report.xlsx'
print(file_name.startswith('report'))
print(file_name.endswith('.xlsx'))
print(file_name.endswith('.ppt'))

# 문자 타입 종류 확인
print('1234'.isdigit())  # 숫자로 바꿀수 있냐
print('123ㄴㄴ4'.isdigit())  # False 숫자형태가 아님

print('abcs'.isalpha())  # 문자로만 이루어져있냐

print('1234'.isalnum())
print('abcd'.isalnum())
print('abcd!>!?>!@?'.isalnum())  #숫자,영문으로만 이루어져 있냐

# 메소드 체이닝 (이어붙여서 수행)
raw = '         Hello, Python    '
raw = raw.strip().lower().replace('python','World').title()
print(raw)

#이메일
email = input('이메일 :').strip().lower()  # 공백제거, 소문자로
print(email)
user_id, domain = email.split('@')
print(user_id,domain)