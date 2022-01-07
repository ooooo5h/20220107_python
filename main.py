# FCM 서버에 파이썬 프로그램으로 API 호출 (기기 푸시알림 전송 요청)
import requests

# 함수 제작 : 보내줄 문구/본문 내용을 받아서 전송
def send_fcm_notification(title, body) :
    
    # FCM서버에 요청
    # 1. 호스트 주소/기능 주소 결합 => 실제 기능 URL
    url = 'https://fcm.googleapis.com/fcm/send'
    
    # 2. 첨부해야할 파라미터(보내줄 데이터)
    # 헤더에, 인증키 (token같은 개념)를 담아서 전달
    headers = {
        'Authorization' : 'key=AAAAIa5pqTE:APA91bEHapMzDNGFdrQGHrlxyNifVPyA1cSfypmDq94BWtX6QlRFq9OJPhE-gO1yk9y0ichwd8DBNeeAgtPltUiypiA-6z1FtK0YCxgnjUtOiN767MU0RYYTWGG8h6PCZ7Qazl9xPRmy',
        'Content-Type' : 'appication/json; UTF-8,'       
    }