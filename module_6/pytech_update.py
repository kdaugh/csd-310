#Kevin Daugherty
#Assignment 6.2
#January 22, 2023

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.mohdojv.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# get and find the students collection 
students = db.students 
student_list = students.find({})

# output message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop through collection then output results 
for s in student_list:
    print("  Student ID: " + s["student_id"] + "\n  First Name: " + s["first_name"] + "\n  Last Name: " + s["last_name"] + "\n")

# update last_name of student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Schmidt"}})

# find the updated student document 
jake = students.find_one({"student_id": "1007"})

# output message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output the updated document to the terminal window
print("  Student ID: " + jake["student_id"] + "\n  First Name: " + jake["first_name"] + "\n  Last Name: " + jake["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")