import sqlite3
from flask import Flask, render_template, request, redirect, url_for,session,flash


app = Flask(__name__)
app.secret_key = "dev_secret_key"

# --------
# DATABASE CONNECTION
#--------
def get_db():
    conn = sqlite3.connect('flask_auth.db')
    conn.row_factory = sqlite3.Row
    return conn

# --------
# LOADING PAGE
#--------
@app.route('/')
def home():
    return redirect(url_for('login'))

#-----------
# LOGIN ROUTE
#-----------
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? and password = ?", (email, password))
        user = cursor.fetchone()
        conn.close()


        if user:
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password')
            
    return render_template('login.html')

#-----------
# DASHBOARD ROUTE
#-----------
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username = session['username'])
    return redirect(url_for('login'))

#-----------
# SIGNUP ROUTE
#-----------
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = get_db()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
            conn.commit()
            flash("account created successfully! Please login.")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Email already exists. Please use a different email.")
        finally:
            conn.close()
            

    return render_template('signup.html')

#-----------
# LOGOUT ROUTE
#-----------
app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

#-----------
# RUN APP
#-----------
if __name__ == '__main__':
    app.run(debug=True)
