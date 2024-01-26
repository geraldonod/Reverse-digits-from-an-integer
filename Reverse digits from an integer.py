#ask user for an integer
number = int(input("Enter a number: "))
print("Given number", number)

#loop that reverses the digits
while number > 0:
    digit = number % 10
    number = number // 10
    print(digit, end=" ")
