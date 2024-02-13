from alchemyConnect import *


# create subroutine
def insert_data():
    
    # memberID, Firstname, Surname, DOB, Address, City
    # with primary key auto incremented:

    fName = input("Enter Firstname: ")
    sName = input("Enter Surname: ")
    dob = input("Enter DOB: ")
    address = input("Enter address: ")
    city = input("Enter city: ")

    # without primary key auto incremented:
    # mId = int(input("Enter memberID: "))
    # fName = input("Enter Firstname: ")
    # sName = input("Enter Surname: ")
    # dob = input("Enter DOB: ")
    # address = input("Enter address: ")
    # city = input("Enter city: ")

    # create members list 
    members = []
    # "method 1"
    members.append(fName)
    members.append(sName)
    members.append( dob)
    members.append(address)
    members.append( city)
    # # or 
    # # method 2 
    # members.extend([fName,sName,dob,address, city])xxx

    try:
        # dbCursor.execute("INSERT INTO members VALUES(NULL, %s, %s,%s,%s,%s)", (fName,sName, dob, address, city))
        # or 
        dbCursor.execute("INSERT INTO members VALUES(NULL, %s, %s,%s,%s,%s)", members)

        dbCon.commit()
    except sql.errors.Error as e:
        print(f"Failed : {e}")

if __name__ == "__main__":
    insert_data()  

