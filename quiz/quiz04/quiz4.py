# 문제 1

age = int(input('나이를 입력하시오 :'))
if age < 8 :
    print('무료')
elif 8<=age<=13 :
    print('650원')
elif 14<=age<=18 :
    print('1050원')
elif 19<=age<=64 :
    print('1350원')
elif 65<=age :
    print('무료')
else :
    print('잘못된 입력입니다.')    


# 문제 2

year = int(input('년도를 입력하시오 :'))
if year % 400 == 0:
    print('윤년')
elif year % 100 == 0:
    print('윤년아님')   
elif year % 4 == 0:
    print('윤년')     
else :
    print('윤년아님')

# if year%400 == 0 or(year%4==0 and year%100 != 0) :
#     print('윤년')
# else :
#     print('윤년아님')

# 문제 3

rest = 9000
cost = 0 if age<8 else 650 if age <= 13 else 1050 if age<=18 else 1350 if age <= 64 else 0
print(rest-cost)

# 문제 4
q,w,e = map(int, input('세 정수를 입력하시오 : ').split())
if q==w==e :
    print(q,w,e)
elif q==w :
    if q>e :
        print(q,w)    
    else :
        print(e)    
elif q==e     :
    if q>w :
        print(q,e)
    else :
        print(w)
elif w==e :
    if w>q :
        print(w,e)
    else :
        print(q)          
elif q>w:
    if w>e :
        print(q)
    else :
        if q > e:
            print(q)
        else :
            print(e)
elif w>q :
    if w>e:
        print(w)
    else :
        print(e)   

# if q >= w and q >= e:
#     print(q)
# elif w>=q and w>=e : 
#     print(w)
# else :
#     print(e)   간결하게

print(max(q,w,e))