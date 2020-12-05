
class ValidateYear:
    def __init__(self, max_year, min_year):
        self.max_year = max_year
        self.min_year = min_year

    def validate(self, year):
        return len(year) == 4 and int(year) >= self.min_year and int(year) <= self.max_year

class HeightValidation:
    def __init__(self):
        pass

    def validate(self, height):
        height_num = height[0:-2]
        if len(height_num) == 0:
            return False
        height_num = int(height_num)
        if height[-2:] == 'cm':
            return height_num >= 150 and height_num <= 193
        if height[-2:] == 'in':
            return height_num >= 59 and height_num <= 76
        return False

class HairColorValidation:
    def __init__(self):
        pass

    def validate(self, color):
        if len(color) != 7:
            return False
        if not color.startswith('#'):
            return False
        i = 1
        while i < len(color):
            if not (color[i].isdigit() or color[i] in ['a', 'b', 'c', 'd', 'e', 'f']):
                return False
            i += 1
        return True

class EyeColorValidation:
    def __init__(self):
        pass

    def validate(self, color):
        return color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

class PassportValidation:
    def __init__(self):
        pass

    def validate(self, pid):
        if len(pid) != 9:
            return False
        for n in pid:
            if not n.isdigit():
                return False
        return True


REQUIRED_FIELDS = {
    'byr': ValidateYear(2002, 1920),
    'iyr': ValidateYear(2020, 2010),
    'eyr': ValidateYear(2030, 2020),
    'hgt': HeightValidation(),
    'hcl': HairColorValidation(),
    'ecl': EyeColorValidation(),
    'pid': PassportValidation(),
}



def is_valid(field, use_rules=False):
    field_name = field.split(':')[0]
    field_value = field.split(':')[1]
    if field_name not in REQUIRED_FIELDS:
        return False
    if not use_rules:
        return True
    validation = REQUIRED_FIELDS[field_name].validate(field_value)
    return validation


def find_num_valid(use_rules=False):
    num_valid = 0
    with open('input.txt', 'r') as reader:
        fields = set()
        for line in reader:
            split_spaces = line.split()
            if len(split_spaces) == 0:
                if len(fields) == 7:
                    num_valid += 1
                fields = set()

            for field in split_spaces:
                if is_valid(field, use_rules=use_rules):
                    fields.add(field.split(':')[0])

        if len(fields) == 7:
            num_valid += 1
    return num_valid

print('Num valid passports part 1: {}'.format(find_num_valid()))
print('Num valid passports part 2: {}'.format(find_num_valid(use_rules=True)))