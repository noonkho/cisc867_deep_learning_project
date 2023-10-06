"""
Perform a train_test k-fold validation split.
k = 5 currently so we always train with 80% of the patient cases and leave 20% as holdout

Code from https://www.kaggle.com/code/carnozhao/uwmgit-mmsegmentation-end-to-end-submission
"""

import glob
import os

all_image_files = glob.glob("./data/train/*/*")
patients = [os.path.basename(_).split("_")[0] for _ in all_image_files]

from sklearn.model_selection import GroupKFold

split = list(GroupKFold(5).split(patients, groups=patients))

for fold, (train_idx, valid_idx) in enumerate(split):
    with open(f"./data/splits/fold_{fold}.txt", "w+") as f:
        fold_set = set()
        for idx in train_idx:
            # fold_set.add(os.path.basename(all_image_files[idx]) + "\n")
            f.write(os.path.basename(all_image_files[idx]) + "\n")
    with open(f"./data/splits/holdout_{fold}.txt", "w+") as f:
        for idx in valid_idx:
            f.write(os.path.basename(all_image_files[idx]) + "\n")
