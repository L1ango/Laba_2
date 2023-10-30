#Написать функцию prime, принимающую 1 аргумент — номер простого числа в последовательности
# простых чисел, и возвращающую само простое число.
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime(n):
    if n <= 0:
        raise ValueError("Порядковый номер должен быть положительным целым числом")
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1

try:
    n = int(input("Введите порядковый номер простого числа: "))
    result = prime(n)
    print(str(n)+"-ое простое число: "+str(result))
except ValueError as e:
    print("Ошибка: "+str(e))
except Exception as e:
    print("Произошла ошибка: "+str(e))
finally:
    print("Программа завершена")