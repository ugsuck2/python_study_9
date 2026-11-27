#문제 1

scores = [88, 92, 75, 64, 95, 81, 70]

print('최고점 :',max(scores))
print('최저점 :',min(scores))
print('평균 :',sum(scores)/len(scores))

up80 = [ i for i in scores if i >= 80]
print(up80)

up80_2 = []
for i  in scores :
    if i >= 80 :
        up80_2.append(i)
print(up80_2)        

print(sorted(scores,reverse=True))

# 문제 2
word = input('단어를 입력하시오 :').split()
print(len(word))
long = 0
for i in range(len(word)) :
    if len(word[i])> long :
        long = len(word[i])

for i in range(len(word)):
    if len(word[i]) == long:
        print(word[i])

five_word = [i.upper() for i in word if len(i) >= 5]
print(five_word)

# max 는 절대값 기준이 아니므로 음수여도 절대값이 제일 크게 출력되게 하려면 max(a,key=abs)
#  쓰면 그 값이 출력된다.


#문제 3

cart = []
while True :  # 계속 입력받아야 하므로 무한반복
    input_text = input('입력칸').split()
    order = 'add'
    delete = 'del'
    exit_flag = False

    for i in range(len(input_text)):
        if input_text[i] == order:
            if input_text[i+1] in cart:
                print('이미 담긴 상품',input_text[i+1])
            else:
                cart.append(input_text[i+1])

        elif input_text[i] == delete:
            if input_text[i+1] in cart:
                cart.remove(input_text[i+1])
            else:
                print('없는 상품',input_text[i+1])
        elif input_text[i] == 'q' :
            exit_flag = True
    if exit_flag :
        break        

    for idx, value in enumerate(cart) :
        print(idx+1,value)

