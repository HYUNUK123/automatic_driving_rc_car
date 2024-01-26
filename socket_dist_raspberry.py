'''
This file is a file that receives the value 
of the distance through socket communication with jetson nano.
'''


import socket

HOST ='192.168.180.216'  # 서버의 IP 주소
# You have to put jetson's ip address in the host.
PORT = 12345            # 서버에서 사용하는 포트 번호

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
            distance_up, distance_diag_left, distance_diag_right = map(float, distances)
        except ValueError:
            continue
        
        # 거리정보를 활용하여 동작을 수행
        print(f"위쪽으로의 거리: {distance_up}")
        print(f"좌측 대각선으로의 거리: {distance_diag_left}")
        print(f"우측 대각선으로의 거리: {distance_diag_right}")