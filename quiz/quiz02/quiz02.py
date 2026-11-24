# 문제 1
url = 'https://www.python.org/downloads'
print(url[0:5])
print(url[8:22])
print(url[-9:])

# 문제 2
n = [-32, 5, 2, -10, 55, 7, 9, 0]
print(n[1::2])
print(n[-1:-4:-1])
print(n[::-1])

# 문제 3
date = '20261102'
date = input('날짜를 입력하세여 (YYYYMMDD) : ')
print(str(date[0:4])+'년'+str(date[4:6])+'월'+str(date[6:])+'일')
print(f'{date[:4]}년 {date[4:6]}월 {date[6:]}일')

# 문제 4
year = (2021, 2022, 2023, 2024, 2025, 2026)
population = (10249679, 10195318, 10143645, 9994195, 9886021, 9810000)
print(year[-1:-4:-1])
print(population[-1:-4:-1])