import math

with open("input_13.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

earliest_departure, bus_schedule = content[0], content[1].split(",")


# part 1
def calculate_bus_departures(departure_time, bus_list):
    bus_sched = {}
    for bus in bus_list:
        if bus != "x":
            closest_departure = math.ceil(int(departure_time) / int(bus))
            bus_sched[bus] = closest_departure * int(bus)
    return bus_sched


def calculate_wait_time_x_bus_id(my_departure_time, bus_departures):
    closest_bus_id = min(bus_departures, key=bus_departures.get)
    wait_time = int(bus_departures.get(closest_bus_id)) - int(my_departure_time)
    return wait_time * int(closest_bus_id)


my_bus_schedule = calculate_bus_departures(earliest_departure, bus_schedule)
print(calculate_wait_time_x_bus_id(earliest_departure, my_bus_schedule))



