1.
* https://roboflow.com/
* robo flow 에서 segmentation 프로젝트를 생성하여 라벨링을 하고 데이터셋을 구축합니다.
* ![스크린샷 2024-01-24 16-36-55](https://github.com/82lilsak/automatic_driving_rc_car/assets/141192357/5b316a6a-b6be-4c4e-80c1-76596255edd4)

* annotate 를 수행 한 후
* ![스크린샷 2024-01-24 16-39-02](https://github.com/82lilsak/automatic_driving_rc_car/assets/141192357/3147dbb1-405b-4b18-99c2-623e5a2dc371) 
* generate 탭에서 데이터셋 버전을 만들고 Preprocessing, Augmentation 을 진행합니다.

2.
* ![스크린샷 2024-01-24 16-41-12](https://github.com/82lilsak/automatic_driving_rc_car/assets/141192357/04565789-0889-4ed1-b8cc-cab3bbff7d83)
* customtrain and Upload 를 눌러 데이터셋과 라벨링 데이터를 다운로드 받습니다. 

3.
* Use this link for next step
* https://docs.ultralytics.com/ko/modes/train/

4.
* open data - data.yaml
* change path  default path ../data/train/images
* Use the absolute or relative path for the path
* ex) /home/data/train/images
* ex) ./data/train/images

5. 
* Run train.py
* if you run terminal
```terminal
cd path
python ./train.py 
```

* if you run vscode or other ide
click run button