#Kevin Daugherty
#January 15 2023
#Module 5.3 Assignment

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.mohdojv.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

Jake = {
    "student_id": 1007,
    "first_name": "Jake",
    "last_name": "Smith",
    "enrollments":  [
        {   
            "term": "Fall",
            "gpa": 3.1,
            "start_date": "August 29, 2022",
            "end_date": "November 19, 2022",
            "courses":  [
                {
                    "course_id": CSD310,
                    "description": "Database Systems",
                    "instructor": "Sanders",
                    "grade": "B",
                },
                {
                    "course_id": CSD315,
                    "description": "Information Systems",
                    "instructor": "Blake",
                    "grade": "B",
                }
            ]
        }
   ]
}

Brad = {
    "student_id": 1008,
    "first_name": "Brad",
    "last_name": "Peterson",
    "enrollments":  [
        {   
            "term": "Fall",
            "gpa": 4.0,
            "start_date": "August 29, 2022",
            "end_date": "November 19, 2022",
            "courses":  [
                {
                    "course_id": CSD310,
                    "description": "Database Systems",
                    "instructor": "Sanders",
                    "grade": "A",
                },
                {
                    "course_id": CSD315,
                    "description": "Information Systems",
                    "instructor": "Blake",
                    "grade": "A",
                }
            ]
        }
   ]
}


Carl = {
    "student_id": 1009,
    "first_name": "Carl",
    "last_name": "Davidson",
    "enrollments":  [
        {   
            "term": "Fall",
            "gpa": 3.5,
            "start_date": "August 29, 2022",
            "end_date": "November 19, 2022",
            "courses":  [
                {
                    "course_id": CSD310,
                    "description": "Database Systems",
                    "instructor": "Sanders",
                    "grade": "A",
                },
                {
                    "course_id": CSD315,
                    "description": "Information Systems",
                    "instructor": "Blake",
                    "grade": "B",
                }
            ]
        }
   ]
}

students = db.students

jake_student_id = students.insert_one(jake).inserted_id

print("\n -- INSERT STATEMENTS -- ") 
print(" Inserted student record Jake Smith into students collection with document_ID " + str(jake_student_id))

brad_student_id = students.insert_one(brad).inserted_id

print(" Inserted student record Brad Peterson into students collection with document_ID " + str(brad_student_id))

carl_student_id = students.insert_one(carl).inserted_id

print(" Inserted student record Carl Davidson into students collection with document_ID " + str(carl_student_id))

input("\n\n  End of program, press any key to exit... ")