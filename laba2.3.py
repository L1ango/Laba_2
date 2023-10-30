#Найти в матрице первый столбец, все элементы которого отрицательны,
# и среднее арифметическое этих элементов.
def find_negative_average(matrix):
    try:
        if not matrix:
            raise ValueError("Матрица пуста")

        num_rows = len(matrix)
        num_cols = len(matrix[0])

        found_column = None
        for col in range(num_cols):
            all_negative = True
            column_sum = 0
            for row in range(num_rows):
                if matrix[row][col] >= 0:
                    all_negative = False
                    break
                column_sum += matrix[row][col]

            if all_negative:
                found_column = col
                break

        if found_column is None:
            raise ValueError("В матрице нет столбца с отрицательными элементами")

        negative_elements = [matrix[row][found_column] for row in range(num_rows)]
        average = sum(negative_elements) / len(negative_elements)
        return average

    except ValueError as e:
        print("Ошибка: "+str(e))
        return None
    finally:
        print("Программа завершена")

def input_matrix():
    try:
        num_rows = int(input("Введите количество строк матрицы: "))
        num_cols = int(input("Введите количество столбцов матрицы: "))

        matrix = []
        for i in range(num_rows):
            row = []
            for j in range(num_cols):
                value = float(input(f"Введите элемент матрицы [{i+1}][{j+1}]: "))
                row.append(value)
            matrix.append(row)

        return matrix
    except ValueError:
        print("Ошибка: Введите числовые значения.")
        return None

# Пример использования
matrix = input_matrix()
if matrix is not None:
    average = find_negative_average(matrix)
    if average is not None:
        print("Среднее арифметическое отрицательных элементов первого столбца:", average)
