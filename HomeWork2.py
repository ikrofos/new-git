
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


# Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем

t = (1.4, 5.76, 0.4, 0.55, 9.5)
print('Минимальное значение: ', min(t))
print('Максимальное значение: ', max(t))

#Комментарий

#Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'],
#соеденить все слова в единую строку, чтобы получилось: 'Earth -> Russia -> Moscow'

l1 = ['Earth', 'Russia', 'Moscow']
print(l1[0] + l1[1] + l1[2])
