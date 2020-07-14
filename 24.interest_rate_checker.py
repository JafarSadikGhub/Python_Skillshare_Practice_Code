balance = input("What is your balance?")

if int(balance)<=50:
    print("You do not qualify for interest")
elif int(balance)<100:
    print("Your interest rate is 1%")
else:
    print("Your interest rate is 2%")
    