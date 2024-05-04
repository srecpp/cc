def count_digits(number):
    num_str = str(number)
    return len(num_str)


numbers = [123, 4567, 891234]

for num in numbers:
    print("Number of digits in", num, "is", count_digits(num))
