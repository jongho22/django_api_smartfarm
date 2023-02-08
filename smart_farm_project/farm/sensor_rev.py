import os
import django
import sys
from datetime import datetime
import threading

# 통신
import paho.mqtt.client as mqtt
import pymongo

# 장고
sys.path.append('C:/Users/home/Desktop/프로젝트/스마트팜_장고/smart_farm_project')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_farm_project.settings')
django.setup()
from farm.models import SensorData

class Sensor(threading.Thread):
    def run(self):
        #파이썬에서 mongodb로 연결한다. 27017은 mongodb에서 설정한 포트번호
        connect_to = pymongo.MongoClient("localhost",27017) 

        # connection에서 test_db라는 카테고리 명을 만들고 
        # 그 밑에 collection 명을 test_dat으로 생성
        mdb = connect_to.test_db
        collection = mdb.test_data

        # 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_subscribe(topic 구독), on_message(발행된 메세지가 들어왔을 때)
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("클라이언트와 연결 되었습니다.")
            else:
                print("Bad connection Returned code=", rc)


        def on_disconnect(client, userdata, flags, rc=0):
            print("연결이 해제 되었습니다.")


        def on_subscribe(client, userdata, mid, granted_qos):
            print("연결 상태 : " + str(mid) + " " + str(granted_qos))


        def on_message(client, userdata, msg):

            #sleep(60)
            # 클라이언트에서 받아온 값을 디코딩
            data_split =str(msg.payload.decode("utf-8")).split(" ")

            #print(len(data_split))

            if len(data_split) < 4 :
                print(f"물주기 모터")
                pass
            else :
                # DB에 data 저장
                SensorData(temp=data_split[0],humi=data_split[1],light=data_split[2],rain=data_split[3],water=data_split[4]).save()
                #print(f"{data_rev_date} => Data 저장 성공")
                print(str(msg.payload.decode("utf-8")))
                #print(data)

        # 새로운 클라이언트 생성
        client = mqtt.Client()
        # 콜백 함수
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.on_subscribe = on_subscribe
        client.on_message = on_message

        # 로컬 아닌, 원격 mqtt broker에 연결
        # address : broker.hivemq.com
        # port: 1883 에 연결
        client.connect('broker.hivemq.com', 1883)

        # test/send_data 라는 topic 구독
        client.subscribe('test/send_data', 1) 

        client.loop_forever()
        #sleep(60)



