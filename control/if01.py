
# if 조건문

# if 조건식 :
#    실행문코드(한칸 들여쓰기)   

x  = 10

if x== 10 :
    print('10입니다.')
else :
    print('10이 아닙니다.')

if x>20 :
    print('20보다 크다')
    print('코드 실행문')
print('if  밖의 실행문')    

# 중첩 if

x = 15
if x >= 10:
    print('10 이상')
    if x == 15 :
        print('15입니다')
    if x > 15:
        print('15보다 크다')    


age = 23
if age>=20 and age < 30 :
    print('20대 맞습니다.')


# if 조건식 True | False

# 값이 들어있는 변수들도 조건으로 사용 가능 (0,'',[],None -> False)

item = []
if item :
    print('리스트안에 데이터가 있습니다.')    

if not item :
    print('리스트안에 데이터가 옶습니다.')   

num = int(input('숫자입력해 :'))

if num < 0 :
    print('음수')

if num == 0 :
    print(0)
if num>0 :
    print('양수')
if num%2 ==0 :
    print('짝수')    