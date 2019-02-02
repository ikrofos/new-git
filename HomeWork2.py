
# Создать лист из 6 любых чисел. Отсортировать его по возрастанию

print("Создать лист из 6 любых чисел. Отсортировать его по возрастанию")

list = [3, 4, 3.4, 34, 23, 5]
list.sort()
print(list)

# Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно

print("Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно")
dictionary = {1:'1',
        2:'2',
        3:'3',
        4:'4',
        5:'5',
        6:'6',
        }

for key, value in dictionary.items():
    print (key, value)


# Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы
print('Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы')
matrix = [
            [12, 3, 5, 6],
            [5, 67, 86, 43],
            [45, 67, 85, 5]
        ]

all_row = []
for row in matrix:
    all_row.append(row)
print(all_row)

a = []
b = []
c = []
d = []
for col in matrix:
    a.append(col[0])
    b.append(col[1])
    c.append(col[2])
    d.append(col[3])
print(a, b, c, d)



# Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс

any_obj = [1, 'error', [12, 13, 14], 'True, None, True', 3.1415, 2.718]

for item in any_obj:
    print('Объект:', item, ', его индекс', any_obj.index(item))


# Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'

print('Удалить из списка элементы со значением "to-delite": ')

obj_list = ['to-delite', 3.14, 'to-delite', 2,718, 'to-delite']
for i in obj_list:
    if i == 'to-delite':
        obj_list.remove(i)

print('Полученный список', obj_list)




# Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль

for num in range(10, 0, -1):
    print('инверсия числового вывода: ',  num)
