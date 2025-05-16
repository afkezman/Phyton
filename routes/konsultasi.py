# routes/konsultasi.py
from flask import Blueprint, render_template, request
from app.models import ChatHistory  # Misalnya kita simpan riwayat chat

konsultasi = Blueprint('konsultasi', __name__)

@konsultasi.route('/konsultasi', methods=['GET', 'POST'])
def konsultasi():
    if request.method == 'POST':
        user_message = request.form['message']
        # Simulasi AI yang merespons pesan (gunakan Firebase atau model AI di sini)
        ai_response = "Ini adalah jawaban otomatis dari AI terkait Diabetes."

        # Simpan riwayat chat ke database
        chat_history = ChatHistory(user_message=user_message, ai_response=ai_response)
        db.session.add(chat_history)
        db.session.commit()

        return render_template('konsultasi.html', ai_response=ai_response, user_message=user_message)
    
    return render_template('konsultasi.html', ai_response=None)

