import connectdb as cndb
dir(cndb)
username = input("Username: ")
password = input("Password: ")

activeusers = [["face","123456"]]

for i in activeusers:
    # print(i[0])
    if username == i[0] and password == i[1]:
        print(f"success,  Welcome {username}")
        details = ("name","dob","idtype","id_number","contact_info","dor")
        patient = []
        for j in details:
            j = input(f"Input patient: {j} ")
            patient.append(j)
        patientID = 'MH001'
        patient.insert(0,patientID)
        patient.insert(len(patient), username)
        cndb.savePatientDetails(patient)
        print(patient)
    elif username != i[0]:
        print("User not found")
    else:
        print("Incorrect Username or password")


