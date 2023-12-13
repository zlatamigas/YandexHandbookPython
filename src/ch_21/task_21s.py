name = input()
price = int(input())
weight = int(input())
paid = int(input())

print('=' * 16, 'Чек', '=' * 16, sep='')
print('Товар:', f'{name: >29}', sep='')

cost = price * weight
scost_f = f'{weight}кг * {price}руб/кг'

print('Цена:', f'{scost_f: >30}', sep='')
rubpat = '{}руб'
print('Итого:', f'{rubpat.format(cost): >29}', sep='')
print('Внесено:', f'{rubpat.format(paid): >27}', sep='')
print('Сдача:', f'{rubpat.format(paid - cost): >29}', sep='')
print('=' * 35)
