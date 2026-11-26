for i in range(1,101) :
    if i%15 == 0 :
        print('FizzBuzz',i)
        continue
    elif i%5 == 0:
        print('Buzz',i)
        continue
    elif i%3 == 0 :
        print('Fizz',i)       
        continue
    print(i)     