numbers = set()
with open('input.txt', 'r') as reader:
    for line in reader:
        num = int(line)
        expected_num = 2020 - num
        if expected_num in numbers:
            print(num)
            print(expected_num)
            print(num * expected_num)
            break
        numbers.add(num)