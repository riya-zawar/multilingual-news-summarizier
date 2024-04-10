from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import bcrypt

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Mock database (replace with actual database)
users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users.append({'username': username, 'email': email, 'password': hashed_password})

    return jsonify({'message': 'User registered successfully'})

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    for user in users:
        if user['email'] == email:
            if bcrypt.checkpw(password.encode('utf-8'), user['password']):
                session['email'] = email
                return jsonify({'message': 'Login successful'})

    return jsonify({'message': 'Invalid credentials'})

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
