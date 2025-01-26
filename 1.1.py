first = 10
print(first)
print(id(first)) # id(переменная)-адресс переменной в ram
first = 'Строка'
print(first)
print(id(first))
# Однострочный
'''
Многострочный
комментарий
здесь
'''

first, second, third = 1, 'Строка', 1.7
print(first)
print(third)
print(second)
print(first, second, third)
print(first, second, third, sep=', ') # sep='разделитель'
print(second, end=', ') # end='окончание строки (\n-новая строка)'
print(third, end='!\n')

del second # функция del удаляет переменную

print(first)
print(third)
# print(second) error





