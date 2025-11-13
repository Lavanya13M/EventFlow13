from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from werkzeug.security import generate_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret123"

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Jungkook@Lav13",  # 👈 replace with your MySQL password
    "database": "eventflow"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO users (email, password_hash, phone_number)
            VALUES (%s, %s, %s)
        """, (email, hashed_password, phone))
        conn.commit()
        cur.close()
        conn.close()

        flash("User registered successfully!")
        return redirect(url_for('event_form'))

    return render_template('form1.html')

@app.route('/event', methods=['GET', 'POST'])
def event_form():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        start_date = request.form['startDate']
        end_date = request.form['endDate']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO events (event_title, event_description, event_start_date, event_end_date)
            VALUES (%s, %s, %s, %s)
        """, (title, description, start_date, end_date))
        conn.commit()
        cur.close()
        conn.close()

        flash("Event created successfully!")
        return redirect(url_for('index'))

    return render_template('form2.html')

if __name__ == '__main__':
    app.run(debug=True)
