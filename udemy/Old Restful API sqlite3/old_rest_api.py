from flask import Flask, request
from flask_restful import Resource, Api, reqparse



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
                return {"student": s_stu}, 200
        return {"student": None}, 404  # update with 404 status code - not found

    def post(self, name):

        if next(filter(lambda x: x["s_name"] == name, student_list), None):  # In this example student name is expected to be unique, err handling (error first approach)
            return {"message": "Student {} already exists, not added to the list!".format(name)}, 400

        data = request.get_json()  # json payload
        student_info = {"s_name": name, "s_classroom": data['classroom'], "s_age": data["s_age"]}
        student_list.append(student_info)
        return student_list, 201  # Update with 201 status code - fulfilled & resource is created

    def delete(self, name):
        # for i in range(len(student_list)):
        #     if student_list[i]["s_name"] == name:
        #         del student_list[i]
        #         return {"message": "Student named as {} deleted".format(name), "new list is:": student_list}

        item_to_del = next(filter(lambda item: item["s_name"] == name, student_list), None)  # OPTIMIZED THE CODE ABOVE using filter and lambda functions
        if item_to_del:
            student_list.remove(item_to_del)
            return {"message": "Student named as {} deleted".format(name), "new list is:": student_list}
        else:
            return {"message": "Student {} doesn't exists, could not be deleted from the list!".format(name)}, 404



    def put(self, name):

        data = request.get_json()

        for i in range(len(student_list)):
            if student_list[i]["s_name"] == name:
                old_classroom = student_list[i]["s_classroom"]
                student_list[i]["s_classroom"] = data["classroom"]
                return{"message": "Classroom for {} is updated from {} to {}".format(name, old_classroom, student_list[i]["s_classroom"])}
        return {"message": "There is no such student in the system!"}, 404


class Students(Resource):
    def get(self):
        if student_list:
            return{"students:": student_list}
        return {"message:": "Student list is empty"}, 404

    def delete(self):
        global student_list
        student_list = []
        return {"message": "All students deleted", "current list": student_list}


api.add_resource(Student, '/student/<string:name>')  # http://127.0.0.1:5000/student/Rolf
api.add_resource(Students, '/students')  # http://127.0.0.1:5000/students

app.run(port=5000, debug=True)
