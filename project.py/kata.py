class NegativeNumbersException(Exception):
    pass

def Add(numbers):
    if numbers[:2] == "//" or "\n" in numbers or "," in numbers:
        if numbers[:2] == "//":
            numbers = numbers[2:]
            a_list = numbers.split("\n")
            delimiter = a_list[0]
            numbers = numbers[len(delimiter)+1:]
            num_list = numbers.replace(delimiter, " ").replace(",", " ").replace("\n", " ").split()
        else:
            num_list = numbers.replace(",", " ").replace("\n", " ").split()
    
        negatives_str = ""
        the_sum = 0
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