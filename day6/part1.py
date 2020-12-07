
def process_questions_and_return_total_count():
    with open('input.txt', 'r') as reader:
        total_count = 0
        group_set = set()
        for line in reader:
            split_spaces = line.split()
            if len(split_spaces) == 0:
                total_count += len(group_set)
                group_set = set()
            for char in line:
                if not char.isspace():
                    group_set.add(char)

        total_count += len(group_set)
    return total_count


print("Total count: {}".format(process_questions_and_return_total_count()))
