from flask import Flask, request, send_file, render_template
import os
from threading import Lock

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
image_path = os.path.join(UPLOAD_FOLDER, 'latest.jpg')
lock = Lock()

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        with lock:
            image = request.files['image']
            image.save(image_path)
        return 'Image uploaded successfully', 200
    return 'No image uploaded', 400

@app.route('/latest')
def latest():
    with lock:
        return render_template('index.html', img=image_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
