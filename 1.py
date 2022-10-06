print('Введите имя')
name = input()
print('Введите фамилию')
surname = input()
print('Введите год рождения')
god = int(input())
print(name, surname, god)
name, surname = surname, name
god += 60
print(name, surname, god)
