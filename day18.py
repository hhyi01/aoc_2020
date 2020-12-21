with open("input_18.txt") as f:
    content = f.readlines()

expressions = [x.strip() for x in content]


# part 1
def evaluate_expression(exp):
    ex = exp.replace(" ", "")
    curr_operator = ""
    curr_num = int(ex[0])
    for i, e in enumerate(ex):
        if e == "+" or e == "*":
            curr_operator = e
        else:
            if curr_operator == "+":
                curr_num += int(e)
            elif curr_operator == "*":
                curr_num *= int(e)
    return curr_num


def apply_op(value1, value2, op):
    if op == "+":
        return value1 + value2
    else:
        return value1 * value2


# modified for part 2
def precedence(operation):
    if operation == "+":
        return 2
    if operation == '*':
        return 1
    return 0


def eval_with_parentheses(sub_expression):
    values = []
    ops = []
    i = 0
    while i < len(sub_expression):
        if sub_expression[i] == " ":
            i += 1
            continue
        elif sub_expression[i] == "(":
            ops.append(sub_expression[i])

        elif sub_expression[i].isnumeric():
            values.append(int(sub_expression[i]))
        elif sub_expression[i] == ")":
            while len(ops) != 0 and ops[-1] != "(":
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(apply_op(val1, val2, op))
            ops.pop()
        else:
            while len(ops) > 0 and precedence(ops[-1]) >= precedence(sub_expression[i]):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(apply_op(val1, val2, op))
            ops.append(sub_expression[i])
        i += 1
    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(apply_op(val1, val2, op))
    return values[-1]


def evaluate_expression_list(expression_list):
    result_sum = 0
    for expression in expression_list:
        curr_result = eval_with_parentheses(expression)
        result_sum += curr_result
    return result_sum


print(evaluate_expression_list(expressions))
