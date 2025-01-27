from sys import getsizeof

info = [1, 2, 3]
print(info)
info2 = [1, 1.7, 'Строка', [4, 5, 'Строка 2']]
print(info2)
names = [
    'Misha', 'Vasya', 'Max',
    'Galya', 'Kolya', 'Vasya'
] # список (изменяемый, занимает больше ram)
print(names)
print(names[0])
print(names[0:-1])
print(names[::-1])

print(names.count('Vasya'))
print(names)
print(names.append('Ilya'),names) # изменяет список внося в конец списка значение в ()

result = names.pop(0) # удаляет из списка элемент с указанным номером и выводит его
print(result)
print(names)

names.sort() # сортировка списка
print(names)

names = [
    'Misha', 'Vasya', 'Max',
    'Galya', 'Kolya', 'Vasya'
] # список (изменяемый, занимает больше ram)

names2 = (
    'Misha', 'Vasya', 'Max',
    'Galya', 'Kolya', 'Vasya'
) # кортеж (неизменяемый, занимает меньше ram)

print(getsizeof(names), names)
print(getsizeof(names2), names2)
print(names2[0])