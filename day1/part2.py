def find_nums_that_add_up(numbers, add_up_to_num=2020):
    matrix = []
    for i in range(0, len(numbers)):
        matrix.append([])
        for j in range(0, len(numbers)):
            matrix[i].append(0)

    for i in range(0, len(numbers)):
        num = numbers[i]
        for j in range(0, len(numbers)):
            matrix[i][j] = matrix[i][j] + num
            if i != j:
                matrix[j][i] = matrix[j][i] + num

    for n in range(0, len(numbers)):
        num = numbers[n]
        for i in range(0, len(numbers)):
            if i != n:
                for j in range(0, len(numbers)):
                    if j != n and i != j and add_up_to_num - matrix[i][j] == num:
                        num1 = numbers[i]
                        num2 = numbers[j]
                        return [num, num1, num2]


numbers = []
with open('input.txt', 'r') as reader:
    for line in reader:
        numbers.append(int(line))

numbers_that_add = find_nums_that_add_up(numbers)
print(numbers_that_add)
multiply_num = 1
for n in numbers_that_add:
    multiply_num *= n
print(multiply_num)