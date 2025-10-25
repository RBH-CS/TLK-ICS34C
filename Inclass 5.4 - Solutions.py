def every_other(l):
    new_list = []

    for i in range(0, len(l), 2):
        new_list.append(l[i])

    return new_list


def bigger_ten(l):
    new_list = []

    for num in l:
        if num > 10:
            new_list.append(num)

    return new_list


def distance_mean(l):
    new_list = []

    avg = sum(l)/len(l)
    
    for i in range(len(l)):
        distance = l[i] - avg
        new_list.append(distance)

    return new_list


# Main program
my_list = [0, -12, 4, 18, 9, 10, 11, -23]
print(distance_mean(my_list))
print(every_other(my_list))
print(bigger_ten(my_list))
