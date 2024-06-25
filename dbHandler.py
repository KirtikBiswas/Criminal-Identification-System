import pymysql

def insertData(data):
    rowId = 0

    try:
        # Establish a connection to the database
        db = pymysql.connect(host="localhost", user="kirtik", password="12345", database="criminals")

        # Create a cursor object
        cursor = db.cursor()
        print("Database connected")

        # Prepare SQL query with parameterized query
        query = "INSERT INTO criminaldata (`name`, `father name`, `mother name`, gender, dob, `blood group`, `identity mark`, nationality, `religion`, crimes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        # Execute SQL query with data as parameters
        cursor.execute(query, (data["Name"], data["Father's Name"], data["Mother's Name"], data["Gender"], data["DOB(yyyy-mm-dd)"], data["Blood Group"], data["Identification Mark"], data["Nationality"], data["Religion"], data["Crimes Done"]))

        # Commit changes
        db.commit()

        # Get the last inserted row ID
        rowId = cursor.lastrowid
        print("Data stored on row %d" % rowId)

    except pymysql.Error as e:
        print("MySQL Error:", e)
        # Rollback in case of error
        db.rollback()

    finally:
        # Close the database connection
        db.close()
        print("Connection closed")

    return rowId

def retrieveData(name):
    id = None
    crim_data = None

    try:
        # Establish a connection to the database
        db = pymysql.connect(host="localhost", user="kirtik", password="12345", database="criminals")


        # Create a cursor object
        cursor = db.cursor()
        print("Database connected")

        # Prepare SQL query with parameterized query
        query = "SELECT * FROM criminaldata WHERE `name` = %s"

        # Execute SQL query with name as parameter
        cursor.execute(query, (name,))

        # Fetch a single row
        result = cursor.fetchone()

        # Process the fetched data
        if result:
            id = result[0]
            crim_data = {
                "Name": result[1],
                "Father's Name": result[2],
                "Mother's Name": result[3],
                "Gender": result[4],
                "DOB(yyyy-mm-dd)": result[5],
                "Blood Group": result[6],
                "Identification Mark": result[7],
                "Nationality": result[8],
                "Religion": result[9],
                "Crimes Done": result[10]
            }
            print("Data retrieved")

    except pymysql.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close the database connection
        db.close()
        print("Connection closed")

    return (id, crim_data)
