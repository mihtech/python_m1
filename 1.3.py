# Методы строк(str)

string1 = 'Строка с каким-то количеством символов "с"'
string2 = "Строка с каким-то количеством символов \"с\""
string3 = '''Строка с 
каким-то 
количеством 
символов "с"'''
print(string1)
print(string2)
print(string3)

print(string1.upper()) # перевод в верхний регистр
print(string1.lower()) # перевод в нижний регистр
print(string1.count('с')) # подсчёт совпадений (указаному символу/строке)
print(string1.replace('с', 'б')) # замена

# print(help(str)) вывод информации по методам к строке

text = "Python"
print(text[0], text[-1])
text = 'Программирование'
print(text[0:6], text[::2], text[::-1],text[0:6:2])

print(ord('\'')) # ord(символ) — возвращает числовое значение символа в таблице Unicode.
print(chr(122)) # chr(число) — возвращает символ из таблицы Unicode по его числовому значению.

print("Строка" in string1)
print("строка" not in string1)
print("строка" in string1)
print("Строка" not in string1)