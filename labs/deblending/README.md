Deep learning hands-on : galaxy deblending
==========================================

Setup
-----
1. Activate the environment
```
conda activate dlastro19
```

2. Install the toolbox
```
cd labs/deblending
pip install .
```

3. Download the data (for testing in your laptopt, you do not need to download the full dataset)
```
python download_data.py        # "mini" dataset for testing ~ 60 Mo
python download_data.py full   # full dataset ~ 4 Go
```

Instructions
------------
The goal of this tutorial is create deep learning models to perform a deblending task (i.e. segment 2 overalpping galaxies in an image), starting first with a detection task and followed by a more complex image regression task.

Since the computation task is large without GPUs, you will design a network archicteture locally, test that it runs and then submit the results to a server on which we will run the training using a complete training set. We will then measure a score on a test set and keep a leaderboard.

1. The 

Each model you create should be placed in a `.py` file whose name **HAS TO** follow the rule `nameofthebinome_submissionname.py`, with a **SINGLE** underscore to separate both names and no other specific character.

Before submitting the model, try that it works first on your computer by running

```
pythom main_detection.py nameofthebinome_submissionname.py
```

Once it works, and ONLY THEN, upload the file to the Google Drive for it to be run on GPU.


Notebook
--------
Get started with the [notebook](deblending_starting_kit.ipynb)


