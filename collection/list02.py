

# 리스트 조작

a = [10,20,30]
a.append(40)

print(a)

# 함수 mothod 메소드
# 특정 객체에 속한 함수 : method

a.append([100,200])

print(a)

b = [1,2,3]
b.extend([4,5,6,7])                #b.append(4,5) 안된다.
print(b)

# 특정위치에 추가 insert
c = [10,20,30]
c.insert(1,500)
print(c)
c.insert(0,100)    #앞 추가
c.insert(len(c),100)#뒤 추가
print(c)

# 리스트 요소 삭제

d = [10,20,30]
print(d.pop()) # 제일 뒤에 요소를 삭제 하면서 반환
print(d)
print(d.pop(0)) # pop(index) 해당 인덱스의 요소 삭제하면서 반환
print(d)

# 값으로 요소 삭제
e = [10,20,30,40,50,20]

e.remove(30)
print(e)
#e.remove(60) 없는값 삭제하면 오류
e.remove(20)    # 처음 나오는 값 한개만 삭제
print(e)

# 검색
e = [10,20,30,40,50,20]
print(e.index(30))   # 해당 값이 위치한 인덱스를 반환 없는 값 입력하면 오류
print(e.count(20))   # 해당 값의 개수를 찾아줌

# 뒤집기
e.reverse()
print(e)

# 정렬
e.sort()
print(e)   #리스트를 오름차순으로 정렬
e.sort(reverse=True)  # 내림차순 정렬
print(e)

# sorted()   vs sort()
q = [1,2,4,5,6,7,9,2,3]
#q.sort()  리스트를 그대로 정렬
w = sorted(q)                       #정렬해서 정렬된 리스트를 반환, 새로운 리스트 반환
print(q)                            #원본 리스트는 유지
print(w)

e = sorted(q,reverse=True)
print(e)
q.sort()     #원본 반영
print(q)


print(sorted(q,reverse=True))
print(e.sort())   #None   e.sort() 내부적으로 정렬을 할뿐, 반환이 없음
print(e)

# 모든 요소 삭제
e.clear()
print(e)    #[] 빈리스트

# 리스트 복사
a = [1,2,3,4]
b = a
print(a is b)
print( a == b) 

a[0] = 99
print(a)
print(b)
a = [1,2,3,4]

b = a.copy()
c = a[:]
d = a[::-1]



print( a == b)    #[1,2,3,4] 값은 동일 True
print(a is b)     # 같은 객체인가?


a[0] = 99

print(a,b,c,d)