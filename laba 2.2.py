#Напишите функцию, которая будет принимать один аргумент. Если в функцию передаётся список,
#найти количество четных чисел. Вывести максимальное число. Удалить все отрицательные элементы из списка.
#Если словарь, Отсортируйте по значению в порядке убывания.
#Число – вывести в обратном порядке.
#Строка – определить количество вхождений каждого символа. Вывести в виде словаря.
#Сделать проверку со всеми этими случаями

def process_argument(input_arg):
    try:
        if isinstance(input_arg, list):
            # Если передан список, найдем количество четных чисел, выведем максимальное число и удалим отрицательные элементы
            even_count = len([x for x in input_arg if x % 2 == 0])
            max_num = max(input_arg)
            input_arg = [x for x in input_arg if x >= 0]
            return {
                "even_count": even_count,
                "max_num": max_num,
                "result_list": input_arg
            }

        elif isinstance(input_arg, dict):
            # Если передан словарь, отсортируем его по значению в порядке убывания
            sorted_dict = dict(sorted(input_arg.items(), key=lambda item: item[1], reverse=True))
            return sorted_dict

        elif isinstance(input_arg, int):
            # Если передано число, выведем его в обратном порядке
            return int(str(input_arg)[::-1])

        elif isinstance(input_arg, str):
            # Если передана строка, определим количество вхождений каждого символа и выведем в виде словаря
            char_count = {}
            for char in input_arg:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            return char_count

        else:
            raise ValueError("Неподдерживаемый тип аргумента")

    except ValueError as e:
        print("Ошибка:"+str(e))
        return None
    except Exception as e:
        print("Произошла ошибка: "+str(e))
        return None
    finally:
        print("Программа завершена")


# Примеры использования
input_list = [1, 2, 3, 4, -5, -6, 7, 8]
input_dict = {"a": 5, "b": 2, "c": 8, "d": 1}
input_int = 12345
input_str = "hello"

print(process_argument(input_list))
print(process_argument(input_dict))
print(process_argument(input_int))
print(process_argument(input_str))