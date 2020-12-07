def calc_number_questions_answered(num_people, group_set, all_answered_yes):
    if all_answered_yes:
        return len(dict(filter(lambda elem: elem[1] == num_people, group_set.items())))
    else:
        return len(group_set)

def process_questions_and_return_total_count(all_answered_yes):
    with open('input.txt', 'r') as reader:
        total_count = 0
        group_set = {}
        num_people = 0
        for line in reader:
            split_spaces = line.split()
            if len(split_spaces) == 0:
                number_questions_answered = calc_number_questions_answered(num_people, group_set, all_answered_yes)
                total_count += number_questions_answered
                num_people = 0
                group_set = {}
                continue

            num_people += 1
            for char in line:
                if char.isspace():
                    continue
                if char in group_set:
                    group_set[char] = group_set[char] + 1
                else:
                    group_set[char] = 1
        total_count += calc_number_questions_answered(num_people, group_set, all_answered_yes)
    return total_count


print("Total count: {}".format(process_questions_and_return_total_count(all_answered_yes=False)))
print("Total count where all answered yes: {}".format(process_questions_and_return_total_count(all_answered_yes=True)))
