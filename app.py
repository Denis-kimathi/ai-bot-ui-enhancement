from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Simulated OTP login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Normally here you'd validate OTP and user
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect(url_for('home'))

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.mkdir('uploads')
    app.run(debug=True)
