name = input()
num = int(input())

print(f'Группа №{num // 100}.')
print(f'{num % 10}. {name}.')
print(f'Шкафчик: {num}.')
print(f'Кроватка: {num // 10 % 10}.')
