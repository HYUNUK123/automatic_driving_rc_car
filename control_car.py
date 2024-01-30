import socket
import RPi.GPIO as GPIO
# import Jetson.GPIO as GPIO
import time
from threading import Thread, Lock

# HOST ='192.168.180.216'  # 서버의 IP 주소
# HOST = '172.20.10.10'
HOST ='192.168.136.216'
PORT = 12345            # 서버에서 사용하는 포트 번호

ENA = 12
IN1 = 2
IN2 = 3

ENB = 13
IN3 = 15
IN4 = 14

Dist_list = [150,150,150]
front = []
left = []
right = []
FRONT_DIST_IDX = 0
LEFT_DIST_IDX = 1
RIGHT_DIST_IDX = 2
def dist_avg(distance_up, distance_left, distance_right):
    if distance_up > 350:
        distance_up = 150
    # if distance_up < 1:
    #     distance_up = 100
    else:
        if len(front) < 5:
            front.append(distance_up)
        else:
            front.pop(0)
            front.append(distance_up)
            
            sum_f = sum(front)
            min_f = min(front)
            max_f = max(front)
            
            avg_f = (sum_f - min_f - max_f) / 3
            Dist_list[0] = avg_f
    
    if distance_left > 350:
        distance_left = 150
    else:    
        if len(left) < 5:
            left.append(distance_left)
        else:
            left.pop(0)
            left.append(distance_left)
            
            sum_l = sum(left)
            min_l = min(left)
            max_l = max(left)
            
            avg_l = (sum_l - min_l - max_l) / 3
            Dist_list[1] = avg_l
    
    if distance_right > 350:
        distance_right = 150
    else:       
        if len(right) < 5:
            right.append(distance_right)
        else:
            right.pop(0)
            right.append(distance_right)
            
            sum_r = sum(right)
            min_r = min(right)
            max_r = max(right)
            
            avg_r = (sum_r - min_r - max_r) / 3
            Dist_list[2] = avg_r

GPIO.setmode(GPIO.BCM)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.HIGH)
GPIO.output(IN4, GPIO.LOW)

# PWM 객체 생성
left_pwm = GPIO.PWM(ENA, 1000) # ENA 핀을 PWM으로 설정, 주파수는 100Hz
right_pwm = GPIO.PWM(ENB, 1000) # ENB 핀을 PWM으로 설정, 주파수는 100Hz
left_pwm.start(0) # PWM 시작, 초기 듀티 사이클은 0%
right_pwm.start(0) # PWM 시작, 초기 듀티 사이클은 0%
    
def forward(left_pwm,right_pwm):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    left_pwm.start(32)
    right_pwm.start(32)

def turn_left(left_pwm,right_pwm):
    # GPIO.output(IN1,GPIO.HIGH)
    # GPIO.output(IN2,GPIO.HIGH)
    # GPIO.output(IN3,GPIO.HIGH)
    # GPIO.output(IN4,GPIO.HIGH)
    # time.sleep(0.05)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    left_pwm.start(45)
    right_pwm.start(45)
    
def turn_right(left_pwm,right_pwm):
    # GPIO.output(IN1,GPIO.HIGH)
    # GPIO.output(IN2,GPIO.HIGH)
    # GPIO.output(IN3,GPIO.HIGH)
    # GPIO.output(IN4,GPIO.HIGH)
    # time.sleep(0.05)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    left_pwm.start(45)
    right_pwm.start(45)

# 서버에 연결
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print(f"서버에 연결되었습니다.")

    while True:
        # 서버로부터 거리 정보 수신
        data = client_socket.recv(1024)
        
        if not data:
            print("break")
            break  # 연결이 끊어지면 종료
        try:
        # 수신된 데이터를 파싱하여 거리 정보 추출
            distances = data.decode().split('/')
            distance_up, distance_left, distance_right = map(float, distances)
            dist_avg(distance_up, distance_left, distance_right)
            # 거리정보를 활용하여 동작을 수행
            # print(f"위쪽으로의 거리: {Dist_list[FRONT_DIST_IDX]}")
            # print(f"좌측 대각선으로의 거리: {Dist_list[LEFT_DIST_IDX]}")
            # print(f"우측 대각선으로의 거리: {Dist_list[RIGHT_DIST_IDX]}")
        except ValueError:
            continue
        
        print(Dist_list)
        
        forward(left_pwm,right_pwm)
    
        # time.sleep(0.03)

        if Dist_list[FRONT_DIST_IDX]<120:
            if Dist_list[LEFT_DIST_IDX] < Dist_list[RIGHT_DIST_IDX] and Dist_list[LEFT_DIST_IDX] < 100:
                turn_right(left_pwm,right_pwm)
                print('2')
                time.sleep(0.1)
            elif Dist_list[LEFT_DIST_IDX] > Dist_list[RIGHT_DIST_IDX] and Dist_list[RIGHT_DIST_IDX] < 100:
                turn_left(left_pwm,right_pwm)
                print('1')
                time.sleep(0.1)

        elif Dist_list[LEFT_DIST_IDX] <70:
            turn_right
            (left_pwm,right_pwm)
            print('4')
            time.sleep(0.1)

        elif Dist_list[RIGHT_DIST_IDX] < 70:
            turn_left(left_pwm,right_pwm)
            print('5')
            time.sleep(0.1)