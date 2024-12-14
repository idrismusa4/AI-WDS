from flask import Flask, request, render_template, send_file
import cv2
import os
from weapon_detection import WeaponDetectionSystem  

app = Flask(__name__)
detector = WeaponDetectionSystem(model_size='m')
detector.load_model('../runs/detect/weapon_detector13/weights/best.pt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        image_path = os.path.join('static/uploads', file.filename)
        file.save(image_path)
        annotated_image, detections = detector.detect(image_path)
        if annotated_image is not None:
            output_path = os.path.join('static/annotated_images', file.filename)
            cv2.imwrite(output_path, annotated_image)
            return send_file(output_path, mimetype='image/jpeg')
        else:
            return "Detection failed"
    return "File upload failed"

if __name__ == '__main__':
    app.run(debug=True)