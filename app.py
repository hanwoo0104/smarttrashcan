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

@app.route('/latest', methods=["GET", "POST"])
def latest():
    if request.method == "POST":
        action = request.form.get("action")
        if action == "can":
            f = open('result.txt', 'w')
            f.write('can')
            f.close()
        elif action == "plastic":
            f = open('result.txt', 'w')
            f.write('plastic')
            f.close()
        elif action == "vinyl":
            f = open('result.txt', 'w')
            f.write('vinyl')
            f.close()
    with lock:
        return render_template('index.html', img=image_path)
    
@app.route('/result', methods=["GET"])
def getresult():
    f = open('result.txt', 'r')
    lines = f.readlines()
    result = ""
    for line in lines:
        line = line.strip()
        result = line
    f.close()
    f = open('result.txt', 'w')
    f.write('')
    f.close()
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
