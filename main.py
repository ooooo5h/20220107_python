# FCM 서버에 파이썬 프로그램으로 API 호출 (기기 푸시알림 전송 요청)
import requests
import json

from pyfcm import FCMNotification

# 함수 제작 : 보내줄 문구/본문 내용을 받아서 전송
def send_fcm_notification(title, body) :
    
    # FCM서버에 요청
    # 1. 호스트 주소/기능 주소 결합 => 실제 기능 URL
    fcm_url = 'https://fcm.googleapis.com/fcm/send'
    
    # 2. 첨부해야할 파라미터(보내줄 데이터)
    # 헤더에, 인증키 (token같은 개념)를 담아서 전달
    fcm_headers = {
        'Authorization' : 'key=AAAAIa5pqTE:APA91bEHapMzDNGFdrQGHrlxyNifVPyA1cSfypmDq94BWtX6QlRFq9OJPhE-gO1yk9y0ichwd8DBNeeAgtPltUiypiA-6z1FtK0YCxgnjUtOiN767MU0RYYTWGG8h6PCZ7Qazl9xPRmy',
        'Content-Type' : 'appication/json; UTF-8,'       
    }
    
    content = {
        'registration_ids' : 'fGavK4YBTHWXSqdkGyY7cD:APA91bF63mlYpAOASOi8M1zwOonEQyBliuOfjx8nleTCZtqLifYUBooXbLoclPBApDqzPOM4T5OVKvTCQ2t5OUj58BZJ8Yh1nIfJYOWk_Fvmfzj9JUDyJ6FHMdSo5p6NNrWo7_IXQtXn',  # 어느 기기에 보낼건지, 디바이스 토큰 cf) 리스트로 넣으면, 여러 기기에 동시 전송하는 효과가 있음
        'notification' : {
            
            'title' : title,
            'body' : body,
            
            }, # 기본양식의 알림을 전송하겠다는 뜻. 키를 data-message로 보내면, 커스터마이징을 지원함
    }
    
    # 3. 어떤 방식 + 실제 API 호출
    result = requests.post(fcm_url, data=json.dumps(content), headers=fcm_headers)
    print(f'FCM 발송 결과 : {result}')
    

# send_fcm_notification('안녕하세요', '파이썬을 통해서 보내지롱')

def send_fcm_by_library(title, body) :
    push_service = FCMNotification(api_key='AAAAIa5pqTE:APA91bEHapMzDNGFdrQGHrlxyNifVPyA1cSfypmDq94BWtX6QlRFq9OJPhE-gO1yk9y0ichwd8DBNeeAgtPltUiypiA-6z1FtK0YCxgnjUtOiN767MU0RYYTWGG8h6PCZ7Qazl9xPRmy')
    
    device_token = 'fGavK4YBTHWXSqdkGyY7cD:APA91bF63mlYpAOASOi8M1zwOonEQyBliuOfjx8nleTCZtqLifYUBooXbLoclPBApDqzPOM4T5OVKvTCQ2t5OUj58BZJ8Yh1nIfJYOWk_Fvmfzj9JUDyJ6FHMdSo5p6NNrWo7_IXQtXn'
    
    result = push_service.notify_single_device(registration_id=device_token, message_title=title, message_body=body)
    print(result)
    

# send_fcm_by_library('되나?', '파이썬 pyFCM라이브러리로 전송합니다')

def send_sms_message(phone, message):
    aligo_url = 'https://apis.aligo.in/send/'
    aligo_api_key = 'i5m8plmyxhcpwfvty29hbzko2zzgi0nq'
    data = {
        'key' : aligo_api_key,
        'user_id' : 'cho881020',
        'sender' : '01051123237',
        'receiver' : phone,
        'msg' : message,
        'testmode_yn' : 'y'
    }
    
    requests.post(url=aligo_url, data=data)
    
send_sms_message('01090110390', '파이썬으로 문자보내기 정말 가나!?!?')