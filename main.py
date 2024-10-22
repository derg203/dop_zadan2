from random import random, randrange
n = randrange(3,21) #случайное число от 3 до 20
result = []
for i in range( 1 , n ) :  #1 число для кратности
    for j in range( 1 , n ) :   #2 число для кратности
        if i <= j:
            if n % ( i + j ) == 0  :
                result.extend([i,j])
        else:
            continue

print(f'случайное число от 3 до 20 (логин): {n}')
print('делители (пароль):',*result)