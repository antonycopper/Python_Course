# Решение задачи:
# Сначала необходимо получить шестизначное число. 
# Можно ввести его с клавиатуры функцией input(). 
# Затем извлекаем из этого числа цифры и 
# складываем первые три и последние три. 
# Если эти суммы равны, то билет "счастливый", иначе - нет. 
# Наконец, выводим результат на экран.

# Вот, как это можно реализовать на языке Python:

ticket = input("Введите номер билета (6 цифр): ")
sum1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
sum2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
if sum1 == sum2:
    print("yes")
else:
    print("no")


# Пример работы программы:
# Введите номер билета (6 цифр): 385916
# yes

# Введите номер билета (6 цифр): 123456
# no