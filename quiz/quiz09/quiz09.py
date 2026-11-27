scores = [
    ['김철수', 90, 85, 77],
    ['이영희', 72, 95, 88],
    ['박민수', 65, 70, 92],
    ['최지우', 98, 89, 94],
]
#(이름, 국어, 영어, 수학)
# 문제 1

for i in scores :
    print(i[0],'총점 :',i[1]+i[2]+i[3],'평균 :',round((i[1]+i[2]+i[3])/3,2))
    #sum(i[1:])  1인덱스부터 끝까지 총합
    # 아니면 구조 분해 할당 for name, kor, eng, math in scores

# 문제 2    
sub = ['국어','영어','수학']
sum_sub = [0,0,0]

for j in scores :
    sum_sub[0] = sum_sub[0] + j[1]
    sum_sub[1] = sum_sub[1] + j[2]
    sum_sub[2] = sum_sub[2] + j[3]

for idx, value in enumerate(sub) :
    print(value,'평균 :',round(sum_sub[idx]/len(scores),2))

# 문제 3 

total = []
for i in scores :
    total.append(sum(i[1:]))

max_score = max(total)
idx = total.index(max_score)

print(scores[idx][0])

# 문제 4
my_list = [[j for j in range(4)] for i in range(3)]
num = 0
print(my_list)
for i in range(len(my_list)) :
    for j in range(len(my_list[i])) :
        num += 1
        my_list[i][j] = num
print(my_list)        