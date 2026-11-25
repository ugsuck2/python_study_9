
# break 멈추기 # continue 계속 진행(다음턴...으로 건너뛰기)

i = 1
while True:
    print(i)
    i += 1
    if i == 5:
        break
print('-'*50)
for i in range(100):
    print(i)
    if i == 7 :
        break    

for i in range(1,11) :
    if i == 5 :
        break
    print(i,end=' ')
print()    

for i in range(1,11) :
    if i == 5 :
        continue # 건너뛰기  skip
    print(i,end=' ')

print()    

i = 0
while i<10:
    i=i+1
    if i%2==0:
        continue
    print(i,end=" ")    
    # i = i + 1 이 여기오면 무한루프됨    
    # 반복의 조건식이 거짓이 되는 케이스를 만드는 기준 변수의 변화...
    # 반복문이 언제 멈출지 결정하도록 기준이 되는 변수의 값을 바꾸는 것
    # continue 앞 | 뒤
    
print()    

# 메뉴 선택 반복 : 반복입력 q를 입력하면 종료

while True :
    cmd = input('명령어 입력(q입력시 종료)')
    if cmd == 'q' :
        break
    if cmd == '':
        continue
    print('입력한 명령어:', cmd)

# for else       while else
# 해당 반복이 끝까지 다 돌면 else도 실행
for n in [1,3,5,7,8] :
    if n%2 == 0:
        print('짝수 발견')
        break
    #else 여기쓰면 if에 엮인 else
else :  # for에 엮인 else
    print('짝수가 없다.')    
