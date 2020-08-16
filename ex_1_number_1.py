# Задание 1

# 1. Отсортировать все имена в лексикографическом порядке.

names = open("names.txt", encoding='UTF-8')
r = names.read()
new_r = ''.join(c for c in r if c not in '"')
new_r_2 = new_r.split(',')
new_r_2.sort()
for i in new_r_2:
    print(i)

# 2. Посчитать для каждого имени алфавитную сумму – сумму порядковых номеров букв (MAY: 13 + 1 + 25 = 39).
alphabet = dict([tuple(reversed(i)) for i in enumerate('ABCDEFGHIJKLMNOPQRSTUWVXYZ', 1)])

def func_num(names):
    sum_word = sum([alphabet[i] for i in names])
    return sum_word

new_r_3 = new_r.replace(',', ' ')
# это необходимо сделать, потому что у имени ALONSO стоит \n
new_new = new_r_3.replace('\n', '')
new_r_4 = new_new.split(' ')
new_r_4.sort()
names_2 = list(map(func_num, new_r_4))
print(names_2)
# 3.Умножить алфавитную сумму каждого имени на порядковый номер имени в отсортированном списке
# (индексация начинается с 1). Например, если MAY находится на 63 месте в списке,
# то результат для него будет 63 * 39 = 2457.

x = enumerate(names_2, 1)

def func_index(indexn):
    index, n = indexn
    return n * index

names_3 = list(map(func_index, x))
print(names_3)

# 4. Сложить произведения из п. 3 для всех имен из файла и получить число.

names_4 = sum(names_3)

# 5. Вывести полученную сумму.

print(names_4)