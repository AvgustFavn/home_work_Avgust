'''
4. Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
Можно ли при этом не создавать новый список?

'''

arr = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# print(arr)
arr_1 = []

def test():
    arr.append(str(2))
    arr.append("!")

for i in range(len(arr)):
    temporary_list = arr[i].split(" ")
    hm_indexes = len(temporary_list) -1
    temporary_name = temporary_list[hm_indexes]
    name = temporary_name.lower().title()
    arr_1.append(name)
    print('Привет, {}!'.format(name))

test()
arr_2 = []
for i in range(len(arr)):
    str_temporary = "".join(arr[i])
    for char in str_temporary:
        if char.isdigit():
            print("Я нашел число:", char)

symbols = ".,:;!_*-+()/#%&"
for i in range(len(arr)):
    str_temporary = "".join(arr[i])
    for symbol in symbols:
        for char in str_temporary:
            if symbol in char:
                print("Есть символ:", symbol)

# Ответ на : Можно ли при этом не создавать новый список? Нет, нельзя удалять элементы из списка при итерации по списку
