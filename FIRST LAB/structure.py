guess = 3
t = 0
while t<5:
    ans = int(input('guess:'))
    if ans == guess:
        print('you won')
        break
    else:
        print('wrong')
    t +=1
else:
    print('sry your attempt has been completed')