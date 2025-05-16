# routes/edukasi.py
from flask import Blueprint, render_template

edukasi = Blueprint('edukasi', __name__)

@edukasi.route('/edukasi')
def edukasi():
    return render_template('edukasi.html')
