def validateInt(): # create a function to validate integer
    notValid = True # boolean variable
    while notValid: #same as while True
        try:
            num = int(input())
            notValid = False # toggle the value from True to false if the value entered is an integer
        except ValueError:
            print("You must enter a number: ")
    return num


def inputExpectation(min, max):
    while True:
        try:
            num = int(input())
        except ValueError:
            print('Error: wrong input')
        else:
            if(min <= num < max):
                break
            else:
                print(f"\nError: the value is not within permitted range of {min} to {max}\n")
    return num 