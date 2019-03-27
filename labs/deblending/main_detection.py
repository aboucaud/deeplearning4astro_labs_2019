import os
from importlib import import_module

import numpy as np

from dltools.detector import ObjectDetector


def main(filename, mini=False):
    datadir = "data"
    suffix = "_mini" if mini else ""

    X_train = np.load(os.path.join(datadir, f"train_blends{suffix}.npy"))
    Y_train = np.load(os.path.join(datadir, f"train_target_masks{suffix}.npy"))

    X_test = np.load(os.path.join(datadir, f"test_blends{suffix}.npy"))
    Y_test = np.load(os.path.join(datadir, f"test_target_masks{suffix}.npy"))

    modulename = os.path.splitext(filename)[0]

    binome, submission = modulename.split('_')

    os.makedirs(modulename)
    history_file = os.path.join(modulename, f"{modulename}_history.png")
    sample_file = os.path.join(modulename, f"{modulename}_image_sample.png")
    
    print("\n\n\n")
    print(f"Training submission {submission} by {binome}...")
    print("\n\n\n")

    custom_lib = import_module(modulename)
    model = custom_lib.model()

    obj = ObjectDetector(model, batch_size=16, epoch=3, model_check_point=False)

    print("Training...")
    history = obj.fit(X_train, Y_train)

    print("Testing...")
    score = obj.predict_score(X_test.squeeze(), Y_test)
    print(f"Score: {score:.2f}")

    obj.plot_history(history, history_file)
    obj.plot_random_results(X_test, Y_test, sample_file)

    scoreline = f"{binome}\t{submission}\t{score:.3f}"

    if not os.path.exists('results.txt'):
        with open('results.txt', 'w') as f:
            print(f"binome    \tsubmission\tscore", file=f)
            print(f"------    \t----------\t-----", file=f)

    with open('results.txt', 'a') as f:
        print(scoreline, file=f)

    # if os.environ.get('MARC_GPU_SERVER', 0):
    #     import subprocess

    #     FOLDER = "1JcHPdGCaF0FTm8FGKzXSIE670jlK9fJt"
    #     files = [
    #         "{}_train_history.png".format(filename),
    #         "{}.png".format(filename)
    #     ]

    #     upload_delete = "gdrive upload --parent %s {} --delete" % FOLDER
    #     update = "gdrive update --parent %s {}" % FOLDER
    #     for f in files:
    #         subprocess.run(upload_delete.format(f), shell=True)
    #     subprocess.run(update.format('results.txt'), shell=True)

    

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    main(filename, mini=True)
