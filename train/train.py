from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')

model.train(data='../line.yaml', epochs=1000, patience=50, batch=16, imgsz=320)
# set hyper parameter
# We use jetson nano, performance of device is very low, 
# so we need to adjust the hyperparameter value to make the model lightweight.
# So it increases the number of epochs tremendously, and Set a lot of patience.
# imgsz mainly uses 416 to 640 but decided to use 320 for lightweight.


print(type(model.names), len(model.names))

print(model.names)
