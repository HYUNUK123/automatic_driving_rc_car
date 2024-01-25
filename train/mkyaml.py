# yaml 파일을 학습이 가능하도록 경로 를 설정합니다.
# key-value 데이터인 dict 데이터타입으로 data['train'], data['val'], data['nc'], data['names'] 에 넣어주는데,
# 가장 중요한 부분은 데이터 경로 설정입니다.

import yaml

data = { 'train' : './data/train/images/',
         'val' : './data/valid/images/',
         'test' : './data/test/images',
         
         'names' : ['left', 'left-90', 'left-90-triangle', 'left-X', 'right', 'right-90', 'right-90-square', 'right-circle', 'road', 'track-line'],
         'nc' : 10 }

with open('./data/name.yaml', 'w') as f:  
  yaml.dump(data, f)


with open('/home/label_4/name.yaml', 'r') as f:  
  name_yaml = yaml.safe_load(f)
  print((name_yaml))
