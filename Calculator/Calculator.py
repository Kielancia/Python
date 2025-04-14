import art

def add(n1, n2):
    """ Function adding two numbers """
    return n1 + n2

def subtract(n1,n2):
    """ Function subtracting two numbers """
    return n1 - n2

def multiply(n1,n2):
    """ Function multiplying two numbers """
    return n1 * n2

def division(n1,n2):
    """ Function dividing two numbers """
    return n1 / n2

# Dictionary of available operations
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : division
}

def type_checking(n1):
    """ Function checking if user give us a number """
    try:
        n2 = float(n1)
        format(n2,'.2f')
        return n2
    except ValueError:
        n1 = "NaN"
        return n1

restart = True
total = 0

print(art.logo)

first_number = input("What is your first number?: ")

# Infinity loop
while restart:
    # Checking if we have a float number (we are looping from total = first number) or is it our first entry to loop
    if type(first_number) != float:
        # if it is our first entry, we check the type of input from user - look on function type_checking
        checked_first = type_checking(first_number)
    else:
        # if it is our next entry, we know we have a float number so we are skipping the type_checking
        checked_first = first_number
    # loop for listing operations to choose for user
    for operation in operations:
        print(operation)

    chosen_operation = input("Pick an operation: ")
    # we are checking if user chose the available operation, if not we save it as 'undefined'
    if chosen_operation not in operations:
        chosen_operation = "undefined"

    second_number = input("What is your next number?: ")
    # we are checking the type of user's input
    checked_second = type_checking(second_number)
    # if any given input is not a number our total score is also 'NaN'
    if checked_first == "NaN" or checked_second == "NaN" or chosen_operation == "undefined":
        total = "NaN"
    else:
        # if we sure we have two numbers we can proceed with chosen, by user, operation
        total = operations[chosen_operation](checked_first,checked_second)
    # displaying the whole math behind operation
    print(f"{checked_first} {chosen_operation} {checked_second} = {total}")
    # we are asking the user if he wants to continue counting with total score or restart a calculator
    decision = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ")
    # if he wants to continue with total score, we save total as a first_number and start from the top of while loop
    if decision == "y":
        first_number= total
    else:
        # else we are asking for the first number again and starting from the top of while loop
        print("\n" * 20)
        print(art.logo)
        first_number = input("What is your first number?: ")
