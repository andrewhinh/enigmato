# DO NOT RENAME THIS FILE
# This file enables automated judging
# This file should stay named as `submission.py`

# Import Python Libraries
from fastai.vision.all import *
import os
from tqdm import tqdm
from dotenv import load_dotenv
load_dotenv()

TRAIN_PATH = os.getenv('TRAIN_PATH')

class Predictor:
    """
    DO NOT RENAME THIS CLASS
    This class enables automated judging
    This class should stay named as `Predictor`
    """

    def __init__(self):
        """
        Initializes any variables to be used when making predictions
        """
        self.model = load_learner('export.pkl')

    def make_prediction(self, img_path):
        """
        DO NOT RENAME THIS FUNCTION
        This function enables automated judging
        This function should stay named as `make_prediction(self, img_path)`
        INPUT:
            img_path: 
                A string representing the path to an RGB image with dimensions 128x128
                example: `example_images/1.png`
        
        OUTPUT:
            A 4-character string representing how to re-arrange the input image to solve the puzzle
            example: `3120`
        """

        # Preform a prediction on this image using a pre-trained model (you should make your own model :))
        prediction = self.model.predict(img_path)

        return prediction[0]

# Example main function for testing/development
# Run this file using `python3 submission.py`
if __name__ == '__main__':
    predictor = Predictor()
    
    total = correct = 0

    for label in os.listdir(TRAIN_PATH):
        curr_folder = os.path.join(TRAIN_PATH, label)
        for img_path in tqdm(os.listdir(curr_folder)[:200]):
            img = os.path.join(curr_folder, img_path)
            prediction = predictor.make_prediction(img)
            if prediction == label:
                correct += 1
            total += 1
        print("Finished label:", label)
        print("Running accuracy:", correct / total * 100)
        
    print("Total accuracy:", correct / total * 100)