"""
ПЗ от Августа Фавн, задание второе, условия которого:
2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму,
так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Внимание: новый список не создавать!!!
"""

list_for_home_work = [i**3 for i in range(1, 1001, 2)]
list_str_temp = []
val_0 = 0
result = 0
finally_result = 0
for i in range(0, len(list_for_home_work)):
    result = 0
    temporary_val_0 = str(list_for_home_work[i])

    for str_main_list in temporary_val_0:
        val_0 += int(str_main_list)
    if val_0 % 7 == 0:
        result += int(temporary_val_0)
    val_0 = 0

    finally_result += result

#print(finally_result)

for i in range(0, len(list_for_home_work)):
    list_for_home_work[i] += 17

finally_result = 0
for i in range(0, len(list_for_home_work)):
    result = 0
    temporary_val_0 = str(list_for_home_work[i])

    for str_main_list in temporary_val_0:
        val_0 += int(str_main_list)
    if val_0 % 7 == 0:
        result += int(temporary_val_0)
    val_0 = 0
    finally_result += result

#print(finally_result)




