from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


# Create database and table
def init_db():
    conn = sqlite3.connect('students.db')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            email TEXT NOT NULL,
            course TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


# Home page and student registration
@app.route('/', methods=['GET', 'POST'])
def home():

    message = None

    if request.method == 'POST':
        student_name = request.form['student_name']
        email = request.form['email']
        course = request.form['course']

        conn = sqlite3.connect('students.db')

        conn.execute(
            "INSERT INTO students (student_name, email, course) VALUES (?, ?, ?)",
            (student_name, email, course)
        )

        conn.commit()
        conn.close()

        message = "Student registered successfully!"

    # Display student records
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row

    students = conn.execute(
        "SELECT * FROM students ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template(
        'index.html',
        students=students,
        message=message
    )


# Start application
if __name__ == '__main__':
    init_db()
    app.run(debug=True)