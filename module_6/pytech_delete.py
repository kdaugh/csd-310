#Kevin Daugherty
#Assignment 6.3
#01/22/2023

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.mohdojv.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# find and display student data  
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
students = db.students 
student_list = students.find({}) 
for s in student_list:
    print("  Student ID: " + s["student_id"] + "\n  First Name: " + s["first_name"] + "\n  Last Name: " + s["last_name"] + "\n")

# test document 
john = {
    "student_id": 1010,
    "first_name": "John",
    "last_name": "Doe",
    "enrollments":  [
        {   
            "term": "Fall",
            "gpa": 3.2,
            "start_date": "August 29, 2022",
            "end_date": "November 19, 2022",
            "courses":  [
                {
                    "course_id": 310,
                    "description": "Database Systems",
                    "instructor": "Sanders",
                    "grade": "B",
                },
                {
                    "course_id": 315,
                    "description": "Information Systems",
                    "instructor": "Blake",
                    "grade": "B",
                }
            ]
        }
   ]
}

# insert student data and output insert statements
john_doe_id = students.insert_one(john).inserted_id 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(john_doe_id))

# find and display student_id 1010 data
student_john_doe = students.find_one({"student_id": "1010"}) 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_john_doe["student_id"] + "\n  First Name: " + student_john_doe["first_name"] + "\n  Last Name: " + student_john_doe["last_name"] + "\n")

# call the delete_one method to remove the student_test_doc
students.delete_one({"student_id": "1010"})

# find and display student data
new_student_list = students.find({})
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --") 
for s in new_student_list:
    print("  Student ID: " + s["student_id"] + "\n  First Name: " + s["first_name"] + "\n  Last Name: " + s["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")