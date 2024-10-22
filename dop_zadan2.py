from random import random, randrange
n = randrange(3,21) #случайное число от 3 до 20
def get_password(number):
    password = ''
    for i in range(1, n):
        for j in range(2, n):
            if j <= i:
                continue
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password

print(f'логин : {n}')
result = get_password(n)
print('Пароль:',result)