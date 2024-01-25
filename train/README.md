## custom train yolov8 seg model guide


## 1. labelling and make custom dataset
* https://roboflow.com/
* robo flow 에서 segmentation 프로젝트를 생성하여 라벨링을 하고 데이터셋을 구축합니다.
![스크린샷 2024-01-24 16-36-55](https://github.com/82lilsak/automatic_driving_rc_car/assets/141192357/5b316a6a-b6be-4c4e-80c1-76596255edd4)

* annotate 를 수행 한 후
![스크린샷 2024-01-24 16-39-02](https://github.com/82lilsak/automatic_driving_rc_car/assets/141192357/3147dbb1-405b-4b18-99c2-623e5a2dc371) 
* generate 탭에서 데이터셋 버전을 만들고 Preprocessing, Augmentation 을 진행합니다.

## 2. download custom dataset and unzip
![스크린샷 2024-01-24 16-41-12](https://github.com/82lilsak/automatic_driving_rc_car/assets/141192357/04565789-0889-4ed1-b8cc-cab3bbff7d83)
* customtrain and Upload 를 눌러 데이터셋과 라벨링 데이터를 다운로드 받습니다. 
![Screenshot from 2024-01-25 14-32-26](https://github.com/82lilsak/automatic_driving_rc_car/assets/141192357/64124916-c2e2-4e92-b50b-4a5a71c6a886)
* Yolov8 을 선택한 이후에 Get Snipet 을 눌러서 jupyter notebook , cli, direct link 중 1가지의 방법을 선택하여 다운로드 합니다.
* 이후 unzip을 하여 test, valid, train 폴더와 data.yaml 파일을 repo/train/data 폴더에 옮겨줍니다.

![Screenshot from 2024-01-25 14-44-51](https://github.com/82lilsak/automatic_driving_rc_car/assets/141192357/6dd9e04f-c348-462c-9bd4-a3b2b2f3fd35)


## 3. change path data.yaml and name.yaml

Use this link for next step
https://docs.ultralytics.com/ko/modes/train/

open /data/data.yaml

```terminal
cd train/data
gedit ./data.yaml
```
or open vscode, other editer

change path 
* default path ../data/train/images
* Use the absolute or relative path for the path
* ex1) /home/data/train/images
* ex2) ./data/train/images

open mkyaml.py
* You need to modify the same path that you modified data.yaml
* and run mkyaml.py


## 4. Run train.py
you need change this code
* line5
```Python
model.train(data='/yourpath/data/name.yaml', epochs=1000, patience=50, batch=16, imgsz=320)
```
Run train.py terminal or vscode
* if you run terminal
```terminal
cd train
python ./train.py 
```
* if you run vscode or other ide
click run button

## 5. 선택한 model, yaml 파일을 확인합니다.
* 올바르게 시작하였다면 다음과 유사하게 출력되어야 합니다.


Ultralytics YOLOv8.1.5 🚀 Python-3.9.18 torch-2.2.0a0+gitd925d94 CUDA:0 (AMD Radeon RX 6600 XT, 8176MiB)
engine/trainer: task=segment, mode=train, model=yolov8n-seg.pt, data=/home/label_4/line.yaml, epochs=1000, time=None, patience=50, batch=16, imgsz=320......

## 6. 훈련 완료
올바르게 훈련이 완료되었다면, best.pt, last.pt 2개의 모델이 생성됩니다.
![Screenshot from 2024-01-25 15-26-35](https://github.com/82lilsak/automatic_driving_rc_car/assets/141192357/398acfbb-d2dc-4930-a73d-016da4e28a9f)
