with open("input_06.txt") as f:
    content = f.readlines()

survey_answers = [x.strip() for x in content]


# part 1
def parse_survey_answers(survey_batch):
    yes_answers_count = 0
    current_group = set()
    for survey in survey_batch:
        if survey != "":
            for ans in survey:
                current_group.add(ans)
        else:
            yes_answers_count += len(current_group)
            current_group = set()
    yes_answers_count += len(current_group)
    return yes_answers_count


# print(parse_survey_answers(survey_answers))


# part 2
def count_current_group(group_list):
    return len(set.intersection(*group_list))


def parse_survey_answers_all_yes(survey_data):
    yes_ans_count = 0
    curr_group = []
    for survey_ans in survey_data:
        ind_answers = set()
        if survey_ans != "":
            for ans in survey_ans:
                ind_answers.add(ans)
            curr_group.append(ind_answers)
        else:
            yes_ans_count += count_current_group(curr_group)
            curr_group = []
    yes_ans_count += count_current_group(curr_group)
    return yes_ans_count


print(parse_survey_answers_all_yes(survey_answers))
