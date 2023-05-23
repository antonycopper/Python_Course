number = int(input("Введите трехзначное число: "))
digit_sum = sum(int(digit) for digit in str(number))
print(digit_sum)
