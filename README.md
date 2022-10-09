# Enigmato

Automated Image Patch Re-Ordering

## Setup to train and test our model
1. Clone repo.
2. Run `cd src`.
2. Create a python3 venv using `python3 -m venv env` and then `source env/bin/activate` or `<venv>\Scripts\activate.bat`, depending on your OS.
3. Run `pip3 install -r requirements.txt`.
4. Edit `TRAIN_PATH` in `.env` to be the location of your local training folder as downloaded from [here](https://drive.google.com/file/d/1tQTwXA3Z_ISTAZPScEz8baUYqgafRtpQ/view?usp=sharing).
5. For training a new model, run `python3 train_edit.py` to preprocess the training data and create an `export.pkl` file with the code in `predict.ipynb`.
6. Test out the model with `python3 submission.py`.

## Notes
- Built as a project for the [TAMU Datathon Challenge: Puzzle Solver](https://tamudatathon.com/challenges/docs/td_challenge) challenge.
- Achieves ~90% accuracy on a subset of the training data we hold out as the validation set.

## Credit
- [fast.ai](https://www.fast.ai/) for their model training code.
