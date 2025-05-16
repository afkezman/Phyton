from flask import Blueprint, render_template, request
import os
from werkzeug.utils import secure_filename
from model.gemini_predict import predict_with_gemini
from app import app

scan = Blueprint('scan', __name__)

@scan.route('/scan', methods=['GET', 'POST'])
def scan_luka():
    result = None
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join('uploads', filename)
            file.save(filepath)

            result = predict_with_gemini(filepath)

    return render_template('scan.html', result=result)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}
