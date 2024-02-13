from alchemyConnect import *

# create subroutine
def update_data():
    try:
        # print(dbCursor.lastrowid(), "\n")
        idField = input("Enter the memberID to update a record: ")
        
        # select the unique record from the members table
        dbCursor.execute(f"SELECT * FROM members WHERE memberID = {idField}")

        row = dbCursor.fetchone() # return the specific record selected above

        if row == None:
            print(f"No record {idField} exists")
        else:
            fName = input("Enter Firstname: ")
            sName = input("Enter Surname: ")
            dob = input("Enter DOB: ")
            address = input("Enter address: ")
            city = input("Enter city: ")

            dbCursor.execute(f"UPDATE members SET Firstname = '{fName}', Surname = '{sName}', DOB = '{dob}', Address = '{address}', City = '{city}' WHERE memberID = {idField} ")
            dbCon.commit()
            print(f"Record {idField} updated")
        
    except sql.errors.Error as e:
        print(f"failed : {e}")
if __name__ == "__main__":
    update_data()

