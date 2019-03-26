import os
from importlib import import_module

import numpy as np

from dltools.detector import ObjectDetector


def main(filename):
    X_train = np.load("./data/train_blends_mini.npy")
    Y_train = np.load("./data/train_target_masks_mini.npy")

    X_test = np.load("./data/train_blends_mini.npy")
    Y_test = np.load("./data/train_target_masks_mini.npy")

    module = os.path.splitext(filename)[0]

    name, submission = module.split('_')
    print(f"\n\n\n")
    print(f"Training submission {submission} by {name}...")
    print(f"\n\n\n")

    custom_lib = import_module(module)
    model = custom_lib.model()

    obj = ObjectDetector(model)

    print("Training...")
    obj.fit(X_train, Y_train)

    print("Testing...")
    s = obj.predict_score(X_test.squeeze(), Y_test)
    print("Score: ", s)
    

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    main(filename)
