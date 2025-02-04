from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def main():
    with open('class.json', 'r') as json_file:
        data = json.load(json_file)
        name = data['Name']
        roomNumber = data['Room number']
        project = data['Project']
        lecturer = data['Lecturer']
        students = data['Students']
    return render_template('index.html', name=name, roomNumber=roomNumber, project=project, lecturer=lecturer, students=students)

if(__name__ == "__main__"):
    app.run(host='0.0.0.0', port=5000, debug=True)