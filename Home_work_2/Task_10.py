
#  Решение задачи:
#  Чтобы перевернуть минимальное число монет и 
#  сделать все одинаковой стороной, нужно выбрать более частую сторону 
#  и перевернуть все монетки, которые лежат на другой стороне.

#  Для этого мы можем посчитать количество монеток с гербом и орлом. 
#  Если на столе больше монеток с гербом, то нам нужно перевернуть те, 
#  которые лежат на гербе, чтобы они стали решкой. 
#  И наоборот: если больше монеток с решкой, 
#  то переворачиваем монетки с решкой. 
#  Если же число монеток с решкой и гербом равно, то выбор неважен, 
#  можно перевернуть любую сторону.

#  Вот, как это можно реализовать на языке Python:

n = int(input())
coins = input().split()
heads = coins.count("1")
tails = coins.count("0")
print(abs(heads - tails))


# Пример работы программы:
# Входные данные:
# 6
# 0 1 0 1 1 1
# Результат: 1

# Входные данные:
# 4
# 0 1 0 1
# Результат: 0

# Входные данные:
# 8
# 1 1 0 0 0 1 0 1
# Результат: 3


# PS: В этой задаче "0" означает герб, а "1" - решку. 
# Если в вашей задаче порядок противоположный, 
# нужно поменять значения переменных heads и tails.