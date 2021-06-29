with open("test.txt", "r") as file:
    reader = file.read()

    # Separate into list
    reader_list = reader.split(" ")

    reader_list[0], reader_list[1] = int(reader_list[0]), int(reader_list[1])

    # Calculate Months and Offspring
    def total(months, offspring):
        parent, child = 1, 1
        for itr in range(months - 1):
            # Define on same line b/c if not then parent calculate will include updated child
            child, parent = parent, parent + (child * offspring)
        return child

    # Get sample dataset
    print(total(reader_list[0], reader_list[1]))




# Notes:
# n = index/months
# k = # of offspring
