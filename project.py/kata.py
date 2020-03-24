def Add(numbers):
    for char in numbers:
        if char == ",":
            num_list = numbers.split(",")
            the_sum = 0
            for num in num_list:
                the_sum += int(num)
            return the_sum
    if numbers.isdigit():
        return int(numbers)
    elif numbers == "":
        return 0