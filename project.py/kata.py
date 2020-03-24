def Add(numbers):
    if "," in numbers or "\n" in numbers:
        num_list = numbers.replace("\n", " ").replace(",", " ").split()
        the_sum = 0
        for num in num_list:
            the_sum += int(num)
        return the_sum
    elif numbers.isdigit():
        return int(numbers)
    elif numbers == "":
        return 0