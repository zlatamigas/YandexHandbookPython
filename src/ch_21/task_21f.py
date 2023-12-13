name = str(input())
price = int(input())
weight = int(input())
paid = int(input())
cost = price * weight

print('Чек')
print(name, f'{weight}кг', f'{price}руб/кг', sep=' - ')
print(f'Итого: {cost}руб', f'Внесено: {paid}руб', f'Сдача: {paid - cost}руб', sep='\n')
