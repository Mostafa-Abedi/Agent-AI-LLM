from flask import Flask, jsonify, render_template, request, redirect
from werkzeug.utils import secure_filename
from app import create_chain
import os

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
    message = request.form['messageText'].strip()
    file = request.files.get('pdfFile')

    if not file or not file.filename.endswith('.pdf'):
        return jsonify({'status': 'ERROR', 'answer': 'Please upload a valid PDF file.'})

    # Save the uploaded PDF temporarily
    upload_path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(upload_path)

    response = create_chain(upload_path, message)
    os.remove(upload_path)  # Clean up

    return jsonify({'status': 'OK', 'answer': response})


if __name__ == '__main__':
    app.run(debug=True)
