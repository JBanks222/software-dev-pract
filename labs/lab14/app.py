"""
Jalen Banks
Lab 14 - mini blog using flask
March 19, 2026
"""
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="flaskuser",
        password="password123",
        database="blogDB"
    )


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_blog', methods=['POST'])
def add_blog():
    username = request.form.get('username')
    email = request.form.get('email')
    title = request.form.get('blog_title')
    content = request.form.get('content')

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO USERS (username, email) VALUES (%s, %s)",
        (username, email)
    )
    db.commit()

    user_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO blog (user_id, title, content) VALUES (%s, %s, %s)",
        (user_id, title, content)
    )
    db.commit()

    cursor.close()
    db.close()

    return redirect(url_for('blogs'))


@app.route('/blogs')
def blogs():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT blog.id, USERS.username, blog.title, blog.content, blog.created_at "
        "FROM blog JOIN USERS ON blog.user_id = USERS.USERID"
    )
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('blogs.html', blogs=data)


if __name__ == '__main__':
    app.run(debug=True)
