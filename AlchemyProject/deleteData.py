from alchemyConnect import *

# create subroutine
def delete_data():
    try:
        # print(dbCursor.lastrowid(), "\n")
        idField = input("Enter the memberID to delete a record: ")

        # select the unique record from the members table
        dbCursor.execute(f"SELECT * FROM members WHERE memberID = {idField}")

        row = dbCursor.fetchone() # return the specific record selected above

        if row == None:
            print(f"No record {idField} exists")
        else:
            # found record now delete 
            dbCursor.execute(f"DELETE FROM members WHERE memberID = {idField}")
            dbCon.commit()
            print(f"Record {idField} deleted")
    except sql.errors.Error  as e:
        print(f"Database error: {e}")
if __name__ == "__main__":
    delete_data()