# main.py

from flask import Flask, request, jsonify

app = Flask(__name__)
students = []


@app.get("/student")
def get_all_students():
    grade = request.args.get('s')
    if grade:
        return jsonify(list(filter(lambda s: s["grade"] == int(grade), students)))
    return jsonify(students)


@app.get("/student/<student_id>")
def get_student(student_id):
    return jsonify(students[int(student_id)])


@app.post("/student")
def create_student():
    student = request.get_json()
    student["id"] = len(students)
    students.append(student)
    return jsonify(student), 201


@app.route("/")
def home():
    return "Home"


@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John"
    }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200


@app.route("/create-user", methods=["POST"])
def create_user():
    user = request.get_json()
    return jsonify(user), 201


if __name__ == "__main__":
    app.run(debug=True)
