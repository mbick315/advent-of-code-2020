def create_new_dictionary(numbers, previous_dictionary, add_up_to_num):
    new_dictionary = {}
    for sum_num, indices in previous_dictionary.items():
        for i in range(0, len(numbers)):
            other_num = numbers[i]
            if i not in indices:
                new_sum_num = sum_num + other_num
                if add_up_to_num - new_sum_num >= 0:
                    new_indices = indices.copy()
                    new_indices.add(i)
                    new_dictionary[new_sum_num] = new_indices
    return new_dictionary


def find_nums_that_add_up(numbers, add_up_to_num, count_numbers):
    one_num_dict = {}
    for i in range(0, len(numbers)):
        num = numbers[i]
        one_num_dict[num] = {i}
    i = 1
    previous_dictionary = one_num_dict
    while i < count_numbers:
        previous_dictionary = create_new_dictionary(numbers, previous_dictionary, add_up_to_num)
        i += 1

    if add_up_to_num in previous_dictionary:
        indices = previous_dictionary[add_up_to_num]
        return [numbers[i] for i in indices]
    return []


def multiply_numbers(numbers_that_add):
    multiply_num = 1
    for n in numbers_that_add:
        multiply_num *= n
    return multiply_num


def calculate_numbers_that_add_up_to(count_numbers, add_up_to_num=2020):
    numbers = []
    with open('input.txt', 'r') as reader:
        for line in reader:
            numbers.append(int(line))

    numbers_that_add = find_nums_that_add_up(
        numbers=numbers,
        add_up_to_num=add_up_to_num,
        count_numbers=count_numbers
    )
    print(numbers_that_add)
    print(multiply_numbers(numbers_that_add))


print('Result for 2 numbers')
calculate_numbers_that_add_up_to(2)
print('Result for 3 numbers')
calculate_numbers_that_add_up_to(3)