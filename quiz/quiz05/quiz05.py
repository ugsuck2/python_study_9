num = int(input('구구단 출력 :'))

for i in range(1,10) :
    print(f'{num} * {i} = {num*i}')



num2 = int(input('숫자를 입력하시오.'))
sum2even = 0
sum2odd = 0
for i in range(1,num2+1) :
    if i%2 == 0 :
        sum2even = sum2even + i
    elif i%2 == 1 :
        sum2odd = sum2odd + i    
print('짝수 합 :',sum2even,'홀수 합 :',sum2odd)        



x = [49, -17, 25, 102, 8, 62, 21]
for i in range(len(x)) :
    print(x[i]*10,end=' ')
print()

for v in x :
    print(v*10, end=' ')
print()

rest = 13000
cost = 1350
while rest>0 :
    if rest < cost :
            print('남은 금액', rest)
            break                      #논리상 if문이 앞에 와야한다.
    rest = rest - cost    
    print('남은 잔액',rest)
    