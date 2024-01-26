# Project automatic_driving_rc_car
![스크린샷 2024-01-24 17-23-08](https://github.com/82lilsak/automatic_driving_rc_car/assets/141192357/07caad37-a21c-4d2a-845a-1e381990c78f)

* (간략히 프로젝트를 설명하고, 최종 목표가 무엇인지에 대해 기술)
* jetson nano 기기에서 custom dataset 을 이용하여 train 한 model을 pytorch-gpu 를 사용하여 track-line 을
* detect, segmentation 하여 socket 통신으로 데이터를 전송하고, 
* Raspberry Pi 에서 rc car 를 제어 합니다.

## High Level Design

* (프로젝트 아키텍쳐 기술, 전반적인 diagram 으로 설명을 권장)
* ![Adb](https://github.com/82lilsak/automatic_driving_rc_car/assets/141192357/7fefb54c-8916-46ab-b41c-a052b7c7295b)


## Sequence diagram
![Sequence diagram](https://github.com/82lilsak/automatic_driving_rc_car/assets/141192357/cfbc2c43-b472-4f70-b7e9-add9712620ec)



## Clone code

* (각 팀에서 프로젝트를 위해 생성한 repository에 대한 code clone 방법에 대해서 기술)

```shell
git clone https://github.com/82lilsak/automatic_driving_rc_car.git
```

## Prerequite

* (프로잭트를 실행하기 위해 필요한 dependencies 및 configuration들이 있다면, 설치 및 설정 방법에 대해 기술)

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

or use pip install
```terminal
pip install ultralytics
pip install cap_from_youtube
```
* !!!dependencies of the ultralytics package include cv-python, pytorch, numpy, etc...

if u use gpu or cuda device : check the number of the cuda device.
run test_ultralytics.py or add new python file.

```python3
import ultralytics

ultralytics.checks()
```

There will be a similar output to this shape.
* Ultralytics YOLOv8.1.5 🚀 Python-3.9.18 torch-2.2.0a0+gitd925d94 CUDA:0 (AMD Radeon RX 6600 XT, 8176MiB)
* Setup complete ✅ (12 CPUs, 31.2 GB RAM, 177.6/915.3 GB disk)
!!! CUDA:0 !!! 0 == It will output as many graphics devices as you have. 0 ~ n


If you only have one device that can accelerate one cuda, the output will be CUDA:0.

  

## Steps to train

* (custom 학습 을 위해 절차 기술)
<https://github.com/82lilsak/automatic_driving_rc_car/blob/main/train/README.md>

## Steps to run

* (프로젝트 실행방법에 대해서 기술, 특별한 사용방법이 있다면 같이 기술)
1. activate venv
```jetson-terminal
cd ~/
source .venv/bin/activate
```
2. calculate dist on jetson
```
cd /path_to_repo/ \
python3.8 ./socket_dist_jetson.py
```

2. read dist on raspberry_pi
```raspberry_pi_client
adb
```

## Output

* (프로젝트 실행 화면 캡쳐)

![./result.jpg](./result.jpg)

## Appendix

* (참고 자료 및 알아두어야할 사항들 기술)
