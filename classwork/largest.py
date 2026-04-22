def largest_number(one, two, three):
        largest_number = one
        if two > largest_number:
            largest_number = two
        elif three > two:
            largest_number = three
        return largest_number





print(largest_number(3, 523, 1))
