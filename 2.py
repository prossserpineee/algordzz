print('Введите значение 1 катета')
katet1 = int(input())
print('Введите значение 2 катета')
katet2 = int(input())
s = 0.5 * katet1 * katet2
gipotenusa = (katet1**2 + katet2**2)**0.5
p = katet1 + katet2 + gipotenusa
print('Площадь прямоугольного треугольника равна', round(s, 1))
print('Периметр прямоугольного тругольника равен', round(p, 1))
