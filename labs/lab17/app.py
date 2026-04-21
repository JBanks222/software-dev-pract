import os
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
from werkzeug.utils import secure_filename

app = Flask(__name__)

# ----------------------
# Config
# ----------------------
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
db_config = {
    'host': 'localhost',
    'user': 'flaskuser',
    'password': 'password123',
    'database': 'image_app'
}


def get_db_connection():
    return mysql.connector.connect(**db_config)


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS images (
            id INT AUTO_INCREMENT PRIMARY KEY,
            filename VARCHAR(255),
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        '''
    )

    cursor.execute(
        '''
        SELECT COUNT(*)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = %s AND TABLE_NAME = 'images' AND COLUMN_NAME = 'filename'
        ''',
        (db_config['database'],)
    )
    if cursor.fetchone()[0] == 0:
        cursor.execute('ALTER TABLE images ADD COLUMN filename VARCHAR(255)')

    cursor.execute(
        '''
        SELECT COUNT(*)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = %s AND TABLE_NAME = 'images' AND COLUMN_NAME = 'uploaded_at'
        ''',
        (db_config['database'],)
    )
    if cursor.fetchone()[0] == 0:
        cursor.execute('ALTER TABLE images ADD COLUMN uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP')

    conn.commit()
    cursor.close()
    conn.close()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def list_uploaded_images():
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT filename FROM images ORDER BY uploaded_at DESC, id DESC')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [row[0] for row in rows if row and row[0]]


def save_uploaded_image(filename):
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO images (filename) VALUES (%s)', (filename,))
    conn.commit()
    cursor.close()
    conn.close()


def build_unique_filename(filename):
    base, ext = os.path.splitext(filename)
    candidate = filename
    counter = 1

    while os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], candidate)):
        candidate = f"{base}_{counter}{ext}"
        counter += 1

    return candidate


# ----------------------
# Routes
# ----------------------
@app.route('/')
def index():
    images = list_uploaded_images()
    message = request.args.get('message', '')
    return render_template('index.html', images=images, message=message)


@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files.get('image')

    if not file or file.filename == '':
        return redirect(url_for('index', message='Please choose an image to upload.'))

    if not allowed_file(file.filename):
        return redirect(url_for('index', message='File type not allowed. Use png, jpg, jpeg, or gif.'))

    filename = secure_filename(file.filename)
    filename = build_unique_filename(filename)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    try:
        save_uploaded_image(filename)
    except Error:
        return redirect(url_for('index', message='Image uploaded, but saving filename to DB failed.'))

    return redirect(url_for('index', message='Image uploaded successfully.'))


if __name__ == '__main__':
    app.run(debug=True)
