import os
import cv2
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()
TRAIN_PATH = os.getenv('TRAIN_PATH')

for label in os.listdir(TRAIN_PATH):
    curr_folder = os.path.join(TRAIN_PATH, label)
    print("Current label:", label)
    for img_path in tqdm(os.listdir(curr_folder)):
        img = cv2.imread(os.path.join(curr_folder, img_path))
        h, w = len(img), len(img[0])
        box_size = w // 16 # 3 * w // 32

        starts_x = [w//4 - w//8 - box_size, w//4 - w//8 - box_size + w//2, w//4 - w//8 - box_size, w//4 - w//8 - box_size + w//2]
        starts_y = [h//4 - h//8 - box_size, h//4 - h//8 - box_size, h//2 + h//4 - h//8 - box_size, h//2 + h//4 - h//8 - box_size]

        ends_x = [w//4 + w//8 + box_size, w//2 + w//4 + w//8 + box_size, w//4 + w//8 + box_size, w//2 + w//4 + w//8 + box_size]
        ends_y = [h//4 + h//8 + box_size, h//4 + h//8 + box_size, h//2 + h//4 + h//8 + box_size, h//2 + h//4 + h//8 + box_size]

        for start_x, start_y, end_x, end_y in zip(starts_x, starts_y, ends_x, ends_y):
            img = cv2.rectangle(img, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)
        
        cv2.imwrite(os.path.join(curr_folder, img_path), img)