def Add(numbers):
    if "," in numbers or "\n" in numbers:
        num_list = numbers.replace("\n", " ").replace(",", " ").split()
        the_sum = 0
        for num in num_list:
            if int(num) <= 1000:
                the_sum += int(num)
        return the_sum
    elif numbers.isdigit():
        if int(numbers) <= 1000:
            return int(numbers)
        return 0
    elif numbers == "":
        return 0