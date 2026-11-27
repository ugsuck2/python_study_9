# with ~ as 블록이 끝나면 파일을 자동으로 닫아줌
# open() (모드: 'r' 읽기, 'w' 쓰기, 'a'추가)

all_lines = []

with open('order.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lines = [value.strip() for value in line.split(',')]
        all_lines.append(lines)
#print(all_lines)
all_lines[5][2] = all_lines[5][2].rstrip('원')
for i in range(len(all_lines)-1, -1, -1):
    

    if int(all_lines[i][2]) < 0:
        all_lines.remove(all_lines[i])
    elif int(all_lines[i][2]) > 10000:
        all_lines.remove(all_lines[i])
    elif int(all_lines[i][1]) < 0:
        all_lines.remove(all_lines[i])
for i in all_lines :
    i[1] = int(i[1])
    i[2] = int(i[2])      
total_sales = 0
for i in all_lines :
    total_sales = total_sales + i[1]*i[2]
print('최종 결과:', all_lines)
print('총매출 : ',total_sales)