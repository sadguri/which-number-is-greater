a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a<b:
    if a<c:
        print(f'Минимальное число первое: {a}')
    else:
        print(f'Минимальное число третье: {c}')
else:
    if b<c:
        print(f'Минимальное число второе: {b}')
    else:
        print(f'Минимальное число третье: {c}')