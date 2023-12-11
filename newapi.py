from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pymongo
from bson.objectid import ObjectId
from bson import json_util
import json

#pymongo password: Uh2N2oiHgtz39ISR
#2nd's password: mGdTdZNniUVH67ch

app = FastAPI()
conn_str = "mongodb+srv://66010704:mGdTdZNniUVH67ch@cluster1.aenohu2.mongodb.net/?retryWrites=true&w=majority"
try:
    client = pymongo.MongoClient(conn_str)
    print("Successfully Connected to Pymongo")
except Exception:
    print("Pymongo Init Error: " + Exception)

origins = [
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

db = client.university
students = db.students

class Student(BaseModel):
    name: str
    surname: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: str = None
    surname: str = None
    age: int = None
    year: str = None

arr = list(students.find())
print(arr)

@app.get("/")
def index():
    students_list = list(students.find())
    for student in students_list:
        student["_id"] = str(student["_id"])
    return json.loads(json_util.dumps(students_list))

# @app.get("/get-student/{student_id}")
# def get_student(student_id: int = Path(description = "Input the ID of the student you're looking for.", gt = 0)):
#     return students[student_id]

# @app.get("/get-by-name")
# def get_student(name: str = None):
#     matches = {student_id:str(students[student_id]["name"])+" "+str(students[student_id]["surname"])
#             for student_id in students
#             if students[student_id]["name"] == name}
#     return matches if matches else "No Matches"

# @app.post("/create-student/{student_id}")
# def create_student(student_id: int, student: Student):
#     if student_id in students:
#         return "ID Taken"
#     students[student_id] = student.model_dump()
#     return students[student_id]

# @app.put("/update-student/{student_id}")
# def update_student(student_id:int, student: UpdateStudent):
#     if student_id not in students:
#         return "ID does not exist"
    
#     student_dict = student.model_dump()
#     for data in student_dict:
#         if student_dict[data] != None:
#             students[student_id][data] = student_dict[data]

#     return students[student_id]
    