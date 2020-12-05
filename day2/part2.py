def is_valid_password(password, rule_character, first_position, second_position):
    matches_first_position = len(password) >= first_position and password[first_position] == rule_character
    matches_second_position = len(password) >= second_position and password[second_position] == rule_character
    return (matches_first_position and not matches_second_position) \
        or (not matches_first_position and matches_second_position)


num_valid_passwords = 0
with open('input.txt', 'r') as reader:
    for line in reader:
        rule, password = line.split(':')
        rule_nums = rule.split(' ')[0]
        first_position = int(rule_nums.split('-')[0])
        second_position = int(rule_nums.split('-')[1])
        rule_character = rule.split(' ')[1]
        if is_valid_password(password.strip(), rule_character, first_position-1, second_position-1):
            num_valid_passwords += 1
print(num_valid_passwords)
