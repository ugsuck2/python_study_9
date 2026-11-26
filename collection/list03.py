# 리스트 조작

a = [30,20,50,60,10]

for v in a :
    print(v,end=' ')
print()    

for idx, value in enumerate(a) :
    print(idx,value)

i = 0
while i<len(a) :
    print(a[i],end=' ')
    i += 1 
print()   

# 최소값, 최대값

smallest = a[0]
for v in a:
    if v <= smallest:
        smallest = v
print('최소값',smallest)        

largeest = a[0]
for v in a:
    if v >= largeest:
        largeest = v
print('최대값',largeest)   

# 함수 min max sum
print(min(a))
print(max(a))
print(sum(a))
# 평균     총합 / 갯수
print(sum(a)/len(a))


# 리스트 표현식 (리스트 컴프리헨션)
# [식 for 변수 in 반복이가능한객체]

b = [i for i in range(10)]
print(b)

# =>

b = []
for i in range(10) :
    b.append(i)
print(b)    

c = [i*10 for i  in range(1,11)]
print(c)

# 조건붙이기 추가
# [식 for 변수 in 반복이가능한객체 if 조건]
d = [ i for i in range(10) if i % 2 == 0]
print(d)

d = []
for i in range(10):
    if i%2 == 0 :
        d.append(i)
print(d)

e = [i+5 for i in range(10) if i%2 == 1]
print(e)

# 문자열 리스트
words = ['apple','banana','kiwi']
print(words[0].upper())  #대문자 upper 소문자 lower
words_upper = [v.upper() for v in words]
print(words_upper)

words_len = [len(v) for v in words]
print(words_len)

# map 모든 요소들에게 같은 함수를 적용
words_len2 = list(map(len,words))
print(words_len2)

nums = list(map(str,range(5)))
nums2 = list(range(5))
print(nums)
print(nums2)

# 입력값 split -> map적용
x = list(map(int,input('숫자여러개 띄어쓰기로 입력').split()))
print(x)

# 튜플
t = (30,40,30,20,10,20)
print((t.count),(t.index(10)))
print(min(t),max(t),sum(t))
t_even = tuple( i for i in range(10) if i%2 == 0)
print(t_even)
