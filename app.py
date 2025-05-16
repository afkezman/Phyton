from flask import Flask, render_template, request, redirect, url_for
import os
from dotenv import load_dotenv
from model.gemini_predict import predict_with_gemini  # Ganti ke Gemini
from werkzeug.utils import secure_filename

# Load environment (.env)
load_dotenv()

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.environ.get("SECRET_KEY", "devkey")

# Fungsi cek ekstensi file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Halaman Utama
@app.route('/')
def home():
    return render_template('home.html')

# Halaman Scan
@app.route('/scan', methods=['GET', 'POST'])
def scan():
    return render_template(
        'scan.html',
        FIREBASE_API_KEY=os.environ.get('FIREBASE_API_KEY'),
        FIREBASE_AUTH_DOMAIN=os.environ.get('FIREBASE_AUTH_DOMAIN'),
        FIREBASE_PROJECT_ID=os.environ.get('FIREBASE_PROJECT_ID'),
        FIREBASE_STORAGE_BUCKET=os.environ.get('FIREBASE_STORAGE_BUCKET'),
        FIREBASE_MESSAGING_SENDER_ID=os.environ.get('FIREBASE_MESSAGING_SENDER_ID'),
        FIREBASE_APP_ID=os.environ.get('FIREBASE_APP_ID'),
        FIREBASE_MEASUREMENT_ID=os.environ.get('FIREBASE_MEASUREMENT_ID')
    )

# Halaman Edukasi
@app.route('/edukasi')
def edukasi():
    return render_template('edukasi.html')

# Halaman Konsultasi
@app.route('/konsultasi')
def konsultasi():
    return render_template(
        'konsultasi.html',
        FIREBASE_API_KEY=os.environ.get('FIREBASE_API_KEY'),
        FIREBASE_AUTH_DOMAIN=os.environ.get('FIREBASE_AUTH_DOMAIN'),
        FIREBASE_PROJECT_ID=os.environ.get('FIREBASE_PROJECT_ID'),
        FIREBASE_STORAGE_BUCKET=os.environ.get('FIREBASE_STORAGE_BUCKET'),
        FIREBASE_MESSAGING_SENDER_ID=os.environ.get('FIREBASE_MESSAGING_SENDER_ID'),
        FIREBASE_APP_ID=os.environ.get('FIREBASE_APP_ID')
    )

# Halaman Login
@app.route('/login')
def login():
    return render_template('login.html')

# Halaman Register
@app.route('/register')
def register():
    return render_template(
        'register.html',
        FIREBASE_API_KEY=os.environ.get('FIREBASE_API_KEY'),
        FIREBASE_AUTH_DOMAIN=os.environ.get('FIREBASE_AUTH_DOMAIN'),
        FIREBASE_PROJECT_ID=os.environ.get('FIREBASE_PROJECT_ID'),
        FIREBASE_STORAGE_BUCKET=os.environ.get('FIREBASE_STORAGE_BUCKET'),
        FIREBASE_MESSAGING_SENDER_ID=os.environ.get('FIREBASE_MESSAGING_SENDER_ID'),
        FIREBASE_APP_ID=os.environ.get('FIREBASE_APP_ID')
    )

# Halaman Profil
@app.route('/profil')
def profile():
    return render_template('profile.html')

# Halaman Hasil
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Jalankan Aplikasi
if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
