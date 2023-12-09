from flask import Flask, render_template, request

app = Flask(__name__)

absence_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report_absence', methods=['POST'])
def report_absence():
    student_name = request.form.get('student_name')
    absence_reason = request.form.get('absence_reason')

    absence_data[student_name] = absence_reason

    return render_template('absence_recorded.html', student_name=student_name, absence_reason=absence_reason)

@app.route('/view_absences')
def view_absences():
    return render_template('view_absences.html', absence_data=absence_data)

if __name__ == '__main__':
    app.run(debug=True)
