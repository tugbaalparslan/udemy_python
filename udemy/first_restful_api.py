from flask import Flask, request
from flask_restful import Resource, Api



app = Flask(__name__)
api = Api(app)

student_list = [
    {"s_name": "Alice",
     "classroom": "1C",
     "s_age": 13}
]


class Student(Resource):
    def get(self, name):  # can only be accessed via GET method
        for s_stu in student_list:
            if s_stu["s_name"] == name:
                return s_stu
        return {"student": None}, 404  # update with 404 status code - not found


    def post(self, name):
        data = request.get_json()  # json payload
        student_info = {"s_name": name, "s_classroom": data['classroom'], "s_age": data["age"]}
        student_list.append(student_info)
        return student_list, 201  # Update with 201 status code - fulfilled & resource is created

    def delete(self, name):
        for i in range(len(student_list)):
            if student_list[i]["s_name"] == name:
                del student_list[i]
                return {"message": "Student named as {} deleted".format(name), "new list is:": student_list}

    def put(self, name):

        data = request.get_json()
        for i in range(len(student_list)):
            if student_list[i]["s_name"] == name:
                old_classroom = student_list[i]["s_classroom"]
                student_list[i]["s_classroom"] = data["classroom"]
                return{"message": "Classroom for {} is updated from {} to {}".format(name, old_classroom, student_list[i]["s_classroom"])}



class Students(Resource):
    def get(self):
        if student_list:
            return{"students:": student_list}
        return {"Err Msg:": "Student list is empty"}

    def delete(self):
        global student_list
        student_list = []
        return {"message": "All students deleted", "current list": student_list}


api.add_resource(Student, '/student/<string:name>')  # http://127.0.0.1:5000/student/Rolf
api.add_resource(Students, '/students')  # http://127.0.0.1:5000/students


app.run(port=5000, debug=True)
