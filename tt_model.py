from ultralytics import YOLO
import cv2
import random
import numpy as np
from cap_from_youtube import cap_from_youtube


def overlay(image, mask, color, alpha, resize=None):
    """Combines image and its segmentation mask into a single image.

    Params:
        image: Training image. np.ndarray,
        mask: Segmentation mask. np.ndarray,
        color: Color for segmentation mask rendering.  tuple[int, int, int] = (255, 0, 0)
        alpha: Segmentation mask's transparency. float = 0.5,
        resize: If provided, both image and its mask are resized before blending them together.
        tuple[int, int] = (1024, 1024))

    Returns:
        image_combined: The combined image. np.ndarray

    """
    # color = color[::-1]
    colored_mask = np.expand_dims(mask, 0).repeat(3, axis=0)
    colored_mask = np.moveaxis(colored_mask, 0, -1)
    masked = np.ma.MaskedArray(image, mask=colored_mask, fill_value=color)
    image_overlay = masked.filled()

    if resize is not None:
        image = cv2.resize(image.transpose(1, 2, 0), resize)
        image_overlay = cv2.resize(image_overlay.transpose(1, 2, 0), resize)

    image_combined = cv2.addWeighted(image, 1 - alpha, image_overlay, alpha, 0)

    return image_combined


def plot_one_box(x, img, color=None, label=None, line_thickness=3):
    # Plots one bounding box on image img
    tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)


# Load a model
model = YOLO("/home/test_cv/label_5/last.pt")
class_names = model.names
print('Class Names: ', class_names)
colors = [[random.randint(0, 255) for _ in range(3)] for _ in class_names]


# videoUrl = 'https://youtu.be/OMkQu4XxdoM?si=o_BsGjh2rsu--JL5'
videoUrl = 'https://youtu.be/MY0qxYtcJSw?si=wj0_B4mpU5sRi5Of'
cap = cap_from_youtube(videoUrl)
start_time = 0  # skip first {start_time} seconds
cap.set(cv2.CAP_PROP_POS_FRAMES, start_time * cap.get(cv2.CAP_PROP_FPS))
# cap = cv2.VideoCapture()
print('load & read done\n')


while True:
    
    success, img = cap.read()
 
    if not success:
        print('1')
        continue  # 다음 반복을 건너뜀

    h, w, _ = img.shape
    results = model.predict(img, stream=True, imgsz=320, half=True)
    # print(results)
    for r in results:
        boxes = r.boxes  # Boxes object for bbox outputs
        masks = r.masks  # Masks object for segment masks outputs
        probs = r.probs  # Class probabilities for classification outputs

    if masks is not None:
        masks = masks.data.cpu()
        for seg, box in zip(masks.data.cpu().numpy(), boxes):
            seg = cv2.resize(seg, (w, h))
            img = overlay(img, seg, colors[int(box.cls)], 0.4)

            xmin = int(box.data[0][0])
            ymin = int(box.data[0][1])
            xmax = int(box.data[0][2])
            ymax = int(box.data[0][3])

            plot_one_box([xmin, ymin, xmax, ymax], img, colors[int(box.cls)],
                         f'{class_names[int(box.cls)]} {float(box.conf):.3}')
            mask = cv2.resize(seg, (h, w))
            cv2.imwrite('./output1.png', mask)
            
            
            
            if class_names[int(box.cls)] == "track-line":
                a = 50
                b = 20
                if len(box.data)>1:
                    image_center_x = w // 2
                    xmin = int(box.data[0][0])
                    ymin = int(box.data[0][1])
                    xmax = int(box.data[0][2])
                    ymax = int(box.data[0][3])
                    
                    if xmax > image_center_x:
                        xmax = xmin + a
                    if xmin < image_center_x:
                        xmin = xmax - a
                    
                    
                    xmin1 = int(box.data[1][0])
                    ymin1 = int(box.data[1][1])
                    xmax1 = int(box.data[1][2])
                    ymax1 = int(box.data[1][3])
                    
                    if xmax1 > image_center_x:
                        xmax1 = xmin1 + a
                    if xmin1 < image_center_x:
                        xmin1 = xmax1 - a
                    
                    track_line_center_x = (xmin + xmax) // 2
                    track_line_center_x1 = (xmin1 + xmax1) // 2
                    center = track_line_center_x + track_line_center_x1 // 2
                    
                    
                    if center > image_center_x :
                        if center - image_center_x > b:
                            print('turn left') 
                    elif center < image_center_x:
                        if image_center_x - center > b:
                            print('turn right')
                        
                    
                    
                else: 
                    xmin = int(box.data[0][0])
                    ymin = int(box.data[0][1])
                    xmax = int(box.data[0][2])
                    ymax = int(box.data[0][3])
                    
                    track_line_center_x = (xmin + xmax) // 2

                    image_center_x = w // 2
                    
                    if track_line_center_x > image_center_x :
                        if track_line_center_x - image_center_x > b:
                            print('turn left') 
                    elif track_line_center_x < image_center_x:
                        if image_center_x - track_line_center_x > b:
                            print('turn right')
                    
                
                    
                
                    
                    
               

                       
                    
        
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
