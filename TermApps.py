print("Welcome to TermApps! The versatile terminal application written in python!")
app = input("What app would you like to use? ")
if app == "TermCalc":
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    operation = input("Enter Operation here: ")
    if operation == "Addition":
        result = num1 + num2
        print("The answer is", result)
    elif operation == "Subtraction":
        result = num1 - num2
        print("The answer is", result)
    elif operation == "Division":
        result = num1 / num2
        print("The answer is", result)
    elif operation == "Multiplication":
        result = num1 * num2
        print("The answer is", result)
    elif operation == "Powers":
        result = num1 ** num2
        print("The answer is", result)
    else: print("""
    The operation you entered is not supported. If you made a mistake typing, then try again. If you want another operation, just make a pull request and we will add that unit.
    Pull requests like these help TermCalc become better as well as it also helps TermApps become better.Thank You For The Support and Suggestions!
    """)
elif app == "TermWeight":
    weight = float(input("Enter Weight Here: "))
    weight_unit = input("Enter Weight Unit Here: ")
    new_unit_weight = input("Enter New Weight Unit Here: ")
    if weight_unit == "Kilograms" and new_unit_weight == "Pounds":
        result = weight * 2.204623
        print("Your newly converted weight is", result)
    elif weight_unit == "Pounds" and new_unit_weight == "Kilograms":
        result = weight * 0.4535924
        print("Your newly converted weight is", result)
    else: print("""
    The weight units you entered are not supported. If you made a mistake typing, then try again. If you want another unit, just make a pull request and we will add that unit.
    Pull requests like these help TermWeight become better as well as it also helps TermApps become better.Thank You For The Support and Suggestions!
    """)
elif app == "TermHeight":
    height = float(input("Enter Height Here: "))
    height_unit = input("Enter Height Unit Here: ")
    new_unit_height = input("Enter New Height Unit Here: ")
    if height_unit == "Centimeters" and new_unit_height == "Feet":
        result = height * 0.0328084
        print("Your newly converted height is", result)
    elif height_unit == "Feet" and new_unit_height == "Centimeters":
        result = height * 30.48
        print("Your newly converted height is", result)
    elif height_unit == "Centimeters" and new_unit_height == "Meters":
        result = height * 0.01
        print("Your newly converted height is", result)
    elif height_unit == "Meters" and new_unit_height == "Centimeters":
        result = height * 100
        print("Your newly converted height is", result)
    elif height_unit == "Meters" and new_unit_height == "Feet":
        result = height * 3.28084
        print("Your newly converted height is", result)
    elif height_unit == "Feet" and new_unit_height == "Meters":
        result = height * 0.3048
        print("Your newly converted height is", result)
    else: print("""
    The height units you entered are not supported. If you made a mistake typing, then try again. If you want another unit, just make a pull request and we will add that unit.
    Pull requests like these help TermHeight become better as well as it also helps TermApps become better.Thank You For The Support and Suggestions!
    """)
elif app == "TermCurrency":
    money_amount = float(input("Enter Amount of Money: "))
    currency = input("Enter Currency: ")
    new_currency = input("Enter new Currency: ")
    if currency == "USD" and new_currency == "GBP":
        result = money_amount * 0.77
        print("Your newly converted amount of money is", result)
    elif currency == "GBP" and new_currency == "USD":
        result = money_amount * 1.30
        print("Your newly converted amount of money is", result)
    elif currency == "USD" and new_currency == "AED":
        result = money_amount * 3.67
        print("Your newly converted amount of money is", result)
    elif currency == "AED" and new_currency == "USD":
        result = money_amount * 0.27
        print("Your newly converted amount of money is", result)
    elif currency == "GBP" and new_currency == "AED":
        result = money_amount * 4.79
        print("Your newly converted amount of money is", result)
    elif currency == "AED" and new_currency == "GBP":
        result = money_amount * 0.21
        print("Your newly converted amount of money is", result)
    elif currency == "PKR" and new_currency == "AED":
        result = money_amount * 0.01
        print("Your newly converted amount of money is", result)
    elif currency == "AED" and new_currency == "PKR":
        result = money_amount * 75.57
        print("Your newly converted amount of money is", result)
    else: print("The currency you entered is not supported or not spelled right.")
else: print("The App you entered is either not added or mispelled wrong.")
   






