def Add(numbers):
    for char in numbers:
        if char == ",":
            a, b = numbers.split(",")
            the_sum = int(a) + int(b)
            return the_sum
    if numbers.isdigit():
        return int(numbers)
    elif numbers == "":
        return 0