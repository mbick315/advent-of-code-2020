def is_valid_password(password, rule_character, min_num, max_num):
    num_occurring = 0
    for char in password:
        if rule_character == char:
            num_occurring += 1
            if num_occurring > max_num:
                return False
    return num_occurring >= min_num


num_valid_passwords = 0
with open('input.txt', 'r') as reader:
    for line in reader:
        rule, password = line.split(':')
        rule_nums = rule.split(' ')[0]
        min_num = int(rule_nums.split('-')[0])
        max_num = int(rule_nums.split('-')[1])
        rule_character = rule.split(' ')[1]
        if is_valid_password(password.strip(), rule_character, min_num, max_num):
            num_valid_passwords += 1
print(num_valid_passwords)
