from flask import Flask, request, redirect, url_for
import os
import time

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/user/IT курси/Тестові завдання/VPS store/folder'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']

        if file and allowed_file(file.filename):
            start_time = time.time()
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            end_time = time.time()
            duration = end_time - start_time
            return '''
                <h3>Файл успішно завантажено</h3>
                <p>Час завантаження: {} секунд</p>
                <p>Посилання на завантаження: <a href="{}">{}</a></p>
            '''.format(round(duration, 2), url_for('download_file', filename=filename), filename)
    return '''
        <h1>Завантажити файл</h1>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Завантажити">
        </form>
    '''

@app.route('/download/<filename>')
def download_file(filename):
    return redirect(url_for('static', filename='uploads/{}'.format(filename)), code=301)

if __name__ == '__main__':
    app.run(debug=True)

