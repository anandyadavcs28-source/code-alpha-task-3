from flask import Flask, request
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import sqlite3

app = Flask(__name__)

# Example hardcoded password vulnerability (for review purpose)
admin_password = "admin123"

@app.route('/login', methods=['POST'])
def login():

    # User input
    username = request.form['username']
    password = request.form['password']

    # Secure password hashing
    hashed_password = generate_password_hash(password)

    # Database connection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Secure parameterized query
    query = "SELECT password FROM users WHERE username=?"
    cursor.execute(query, (username,))

    result = cursor.fetchone()

    # Secure password verification
    if result and check_password_hash(result[0], password):
        return "Login Successful"
    else:
        return "Invalid Credentials"

if __name__ == '__main__':
    app.run(debug=True)