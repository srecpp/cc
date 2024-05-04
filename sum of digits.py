def digit_sum(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum

number = int(input("Enter a number: "))
print("Sum of digits:", digit_sum(number))
