#문제 1
a , b = input('사각형의 가로, 세로 길이를 한 줄에 공백으로 구분해서 입력').split()
print('넓이 : ' + str(int(a)*int(b)))
print('둘레 : ' + str(int(a)*2+int(b)*2))

# 문제 2
korean, english, math = input('국어, 영어, 수학점수').split(',')
total = int(korean) + int(english) + int(math)
avg = total/3
print('총점 :' + str(total))
print('평균 :' + round(str(avg),2)) # 반올림 함수round 소수점 두번째자리까지 반올림

# 문제 3
second = input()
print(str(int(second)//3600)+'시간'+str((int(second)%3600)//60)+'분'+str(int(second)%60)+'초')

# 문제 4
year,month,date = input('년,월,일').split(',')
print(year,month,date,sep='/') #2026/05/05
print(f'{year}/{month:0>2}/{date:0>2}')  # :0>2 두칸을 차지해라 문자열 숫자형은 {date:02d}
                                        #zfill(2) 위랑 같은 함수