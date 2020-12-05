with open("input_04.txt") as f:
    content = f.readlines()

passports = [x.strip() for x in content]

expected_fields = {
    "byr": "(Birth Year)",
    "iyr": "(Issue Year)",
    "eyr": "(Expiration Year)",
    "hgt": "(Height)",
    "hcl": "(Hair Color)",
    "ecl": "(Eye Color)",
    "pid": "(Passport ID)",
    "cid": "(Country ID)"
}


# part 1
def parse_passports(passport_batch):
    parsed_passports = []
    current_passport = {}
    for line in passport_batch:
        if line != "":
            parsed_line = line.split(" ")
            for line_item in parsed_line:
                line_items = line_item.split(":")
                key, value = line_items[0], line_items[1]
                current_passport[key] = value
        else:
            parsed_passports.append(current_passport)
            current_passport = {}
    parsed_passports.append(current_passport)
    return parsed_passports


def verify_passport(passport, fields_required, optional_field):
    valid_passport = False
    fields_set = set(fields_required.keys())
    passport_set = set(passport.keys())
    common_fields = fields_set.intersection(passport_set)
    if len(common_fields) == len(fields_required):
        valid_passport = True
    else:
        if len(common_fields) == len(fields_required) - 1 and optional_field not in common_fields:
            valid_passport = True
    return valid_passport


# valid_passport_count = 0
# passports_all = parse_passports(passports)
#
# for pp in passports_all:
#     passport_is_valid = verify_passport(pp, expected_fields, "cid")
#     if passport_is_valid:
#         valid_passport_count += 1
#
# print(valid_passport_count)


# part 2
validation_rules = {
    "byr": {
        "length": 4,
        "min": 1920,
        "max": 2002
    },
    "iyr": {
        "length": 4,
        "min": 2010,
        "max": 2020
    },
    "eyr": {
        "length": 4,
        "min": 2020,
        "max": 2030
    },
    "hgt": {
        "cm_min": 150,
        "cm_max": 193,
        "in_min": 59,
        "in_max": 76
    },
    "hcl": {
        "length": 6,
        "start_char": "#"
    },
    "ecl": {
        "colors": {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    },
    "pid": {
        "length": 9
    }
}


def is_all_num(string_to_check):
    numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    all_num = True
    for c in string_to_check:
        if c not in numbers:
            all_num = False
    return all_num


def verify_field(passport_field, field_value, rules):
    if passport_field == "cid":
        return True

    valid_field = False
    rule_set = rules[passport_field]
    if passport_field == "byr" or passport_field == "iyr" or passport_field == "eyr":
        if len(field_value) == rule_set["length"] and rule_set["min"] <= int(field_value) <= rule_set["max"]:
            valid_field = True
            return valid_field
        return valid_field
    if passport_field == "hgt":
        units = ""
        if "in" in field_value:
            units = "in"
        elif "cm" in field_value:
            units = "cm"
        if units != "":
            height = field_value.replace(units, "")
            all_num = is_all_num(height)
            if all_num:
                if units == "cm" and rule_set["cm_min"] <= int(height) <= rule_set["cm_max"]:
                    valid_field = True
                    return valid_field
                elif units == "in" and rule_set["in_min"] <= int(height) <= rule_set["in_max"]:
                    valid_field = True
                    return valid_field
                else:
                    return valid_field
        return valid_field
    if passport_field == "hcl":
        if field_value.startswith(rule_set["start_char"]):
            remaining = field_value.replace(rule_set["start_char"], "")
            is_alphanum = remaining.isalnum()
            if is_alphanum and len(remaining) == rule_set["length"]:
                valid_field = True
                return valid_field
        return valid_field
    if passport_field == "ecl":
        if field_value in rule_set["colors"]:
            valid_field = True
            return valid_field
        return valid_field
    if passport_field == "pid":
        all_num_pid = is_all_num(field_value)
        if all_num_pid and len(field_value) == rule_set["length"]:
            valid_field = True
            return valid_field
        return valid_field
    return valid_field


valid_passport_count = 0
passports_all = parse_passports(passports)

for pp in passports_all:
    passport_is_valid = verify_passport(pp, expected_fields, "cid")
    if passport_is_valid:
        passed_validation = True
        for field in pp:
            field_passed = verify_field(field, pp[field], validation_rules)
            if not field_passed:
                passed_validation = False
        if passed_validation:
            valid_passport_count += 1

print(valid_passport_count)



