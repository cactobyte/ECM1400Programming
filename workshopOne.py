sumOf = 0
while True:
    number = input("Enter a number 4 times or type 'Q': ")

    if number.lower() != "q":
        x = float(number)
        sumOf += x
    else:
        print("The current sum is {}".format(sumOf))





