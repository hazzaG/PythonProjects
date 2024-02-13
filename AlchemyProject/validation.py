def validateInt(): # create a function to validate integer
    notValid = True # boolean variable
    while notValid: #same as while True
        try:
            num = int(input())
            notValid = False # toggle the value from True to false if the value entered is an integer
        except ValueError:
            print("You must enter a number: ")
    return num