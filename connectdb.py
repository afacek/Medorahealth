import sqlite3

conn = sqlite3.connect("medora.db")

cursor = conn.cursor()
def create_users():
    #CREATE A TABLE users this includes all users from the reception, triage nurses, doctors and surgeons
    cursor.execute("""CREATE TABLE users (f_name TEXT,s_name TEXT,surname TEXT, email TEXT, phone_no TEXT, username TEXT, user_level TEXT)""")
def create_patient():
    #CREATE A TABLE patients // entry point for all patients who will be attended  to a unique no which auto increments with prefix MH22-00001. 22 for year of registration
    cursor.execute("""CREATE TABLE patients (patient_ID TEXT NOT NULL, name TEXT, dob TEXT, idtype TEXT, id_number TEXT, contact_info TEXT,dor TEXT,username TEXT)""")
def create_visits():
    #CREATE A TABLE visits // entry point for all patients who will be attended  to.
    cursor.execute("""CREATE TABLE visits (patient_ID TEXT, VisitId TEXT NOT NULL, datevisit TEXT, username, TEXT)""")
def create_triage():
    #CREATE A TABLE triage // entry point for all patients who will be attended  to.
    cursor.execute("""CREATE TABLE triage (VisitId TEXT, bloodPressure INT, Weight INT, Temperature INT, username TEXT)""")



#SAVE DATA
conn.commit()

# Insert  record
def savePatientDetails(patient):
    patient = [
        ('patient_ID', 'name', 'dob', 'idtype', 'id_number', 'contact_info', 'dor','username')
            ]
    """cursor.execute("INSERT INTO patients VALUES (?,?,?,?,?,?,?,?)",patient)
    
    conn.commit()"""
    print("Data saved successfully")

def get_cursor():
    conn = sqlite3.connect("medora.db")
    return conn.cursor()

def select_all_records_by(cursor):
    sql = "SELECT * from patients"
    cursor.execute(sql)
    print(cursor.fetchall())
    #you can use fetchone() to only fetch one record
    print("\nHere is a listing of the rows  in the table\n")
    for row in cursor.execute("SELECT rowid, * FROM patients ORDER BY name"):
        print(row)

def select_using_like(cursor,text):
    print("\nLIKE query results:\n")
    sql = f"""
    SELECT * FROM patient 
    WHERE name LIKE '{text}%'
    """
    cursor.execute(sql)
    print(cursor.fetchall())

def update_triage(visitID,NewTemperature):
    conn = sqlite3.connect("medora.db")
    cursor = conn.cursor()
    sql = f"""
        UPDATE triage
        SET Temperature = '{NewTemperature}'
        WHERE VisitId = '{visitID}'
        """
    cursor.execute(sql)
    conn.commit()

    """if __name__ == '__main__':
        cursor.get_cursor()"""
# select_all_records_by(cursor)
# select_using_like(cursor,text='john')

def delete_patient(patient):
    conn = sqlite3.connect("medora.db")
    cursor = conn.cursor()

    sql = f"""
            DELETE FROM patients
            WHERE author = '{author}'
            """
    cursor.execute(sql)
    conn.commit()

# if __name__ == '__main__':
#     """delete_patient(name='George Nyamu')"""

def view_all():
    conn = sqlite3.connect("medora.db")
    cursor = conn.cursor()

    sql = """
    SELECT * FROM patients
    """
    allitems = conn.execute(sql)
    datav = []
    for row in allitems:
        datav.append(row)
        print("name: ", row[0])
        print("dob: ",row[1])
        print("id_number: ",row[2])
        print("contact_info: ",row[3])
        print("dor; ",row[4])
        print(" \n")


view_all()
