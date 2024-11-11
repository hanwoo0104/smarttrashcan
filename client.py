import cv2
import requests
import time

def capture_and_upload():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if success:
            _, img_encoded = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 50])  # 품질 50%로 압축
            try:
                requests.post('http://158.247.231.38:80/upload', 
                              files={'image': img_encoded.tobytes()})
            except Exception as e:
                print(f"Error uploading image: {e}")
        response = requests.get('http://158.247.231.38:80/result')
        response_text = response.text
        # 여기부터 시리얼통신 코드

if __name__ == "__main__":
    capture_and_upload()
