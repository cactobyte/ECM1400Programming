taxOwed = 0
while True:
    income = int(input("What is your income?: "))
    if income <= 11000:
        taxOwed = 0
    elif income > 11000 & income <= 43000:
        income -= 11000
        taxOwed = income * 0.3
    elif income > 43000 & income <= 150000:
        taxOwed = 32000 * 0.3 + (income-43000)*0.4
    elif income > 150000:
        taxOwed = 32000 * 0.3 + 106999 * 0.4 + (income-150000) * 0.55
    print("You need to pay £{} in tax".format(taxOwed))