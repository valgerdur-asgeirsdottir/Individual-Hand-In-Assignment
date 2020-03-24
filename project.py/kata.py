class NegativeNumbersException(Exception):
    pass

def Add(numbers):
    if "," in numbers or "\n" in numbers:
        num_list = numbers.replace("\n", " ").replace(",", " ").split()
        the_sum = 0
        negatives_str = ""
        for num in num_list:
            if int(num) < 0:
                negatives_str += str(num) + " "
            elif int(num) <= 1000:
                the_sum += int(num) 
        if len(negatives_str) > 0:
            return_str = "Negatives not allowed: " + negatives_str
            raise NegativeNumbersException(return_str)
        return the_sum
    elif numbers.isdigit():
        if int(numbers) <= 1000:
            return int(numbers)
        return 0
    elif numbers == "":
        return 0