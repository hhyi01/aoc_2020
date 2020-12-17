with open("input_16.txt") as f:
    content = f.readlines()

ticket_info = [x.strip() for x in content]

# print(ticket_info)


# part 1
def parse_ticketing_data(ticketing_info):
    notes_and_tickets = {}
    i = 0
    temp_list = []
    while i < len(ticketing_info):
        data = ticket_info[i]
        if data != "":
            temp_list.append(data)
        else:
            first_item = temp_list[0]
            for item in temp_list:
                if ": " in item:
                    items = item.split(": ")
                    key, value = items[0], items[1]
                    notes_and_tickets[key] = value
                if "your ticket" in first_item:
                    key = "your ticket"
                    if key in notes_and_tickets:
                        notes_and_tickets[key] = item
                    else:
                        notes_and_tickets[key] = ""
            temp_list = []
        i += 1
    if len(temp_list) > 0:
        first_item = temp_list[0]
        for t in temp_list:
            if "tickets" in first_item:
                key = "nearby tickets"
                if key in notes_and_tickets:
                    notes_and_tickets[key].append(t)
                else:
                    notes_and_tickets[key] = []
    return notes_and_tickets


def verify_ticket(ticket_ranges, ticket):
    ticket_fields = [int(t) for t in ticket.split(",")]
    invalid_num = 0
    for num in ticket_fields:
        valid_for_one = False
        for field in ticket_ranges:
            rule = ticket_ranges[field].split(" or ")
            range1 = [int(r1) for r1 in rule[0].split("-")]
            range2 = [int(r2) for r2 in rule[1].split("-")]
            if range1[0] <= num <= range1[1] or range2[0] <= num <= range2[1]:
                valid_for_one = True
        if not valid_for_one:
            invalid_num = num
    return invalid_num


def get_notes_only(all_data):
    notes = {}
    for d in all_data:
        if d != "your ticket" and d != "nearby tickets":
            notes[d] = all_data[d]
    return notes


def calculate_scanning_error_rate(ticket_list, field_ranges):
    error_rate_total = 0
    for ticket in ticket_list:
        error_rate = verify_ticket(field_ranges, ticket)
        error_rate_total += error_rate
    return error_rate_total


all_ticket_data = parse_ticketing_data(ticket_info)
notes_only = get_notes_only(all_ticket_data)
nearby_tickets = all_ticket_data['nearby tickets']

print(calculate_scanning_error_rate(nearby_tickets, notes_only))

