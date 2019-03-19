# Morphology of SDSS galaxies

The goal of these exercices is to test on the same problem, 1- a "classical" machine learning approach and a 2 - a deep learning approach (CNNs) to separate SDSS galaxies between ellitpicals (early-type) and spirals (late-type). You can also try more detailed morphologies to see the difference.

## Set up of environment
- If not done yet, go [here](https://github.com/aboucaud/deeplearning4astro_labs_2019) and follow steps 1 and 2 (+3 if you have a GPU)
- Start your virtual environment: source activate dl4astro19
- Go to folder cd deeplearning4astro_labs_2019/morphology
- You might need to install Pillow the first time you activate the environment: conda install -c intel pillow
- Start a jupyter notebook: jupyter notebook&


## Data provided
- The training set is made of the detailed visual classifications of [Nair&Abraham2010](http://adsabs.harvard.edu/abs/2010ApJS..186..427N) of ~14.000 SDSS galaxies. 

The TType column gives the visual classification as follows:
-5--> E
-3 to -2 --> S0
0 --> S0/a
1 --> Sa
2 --> Sab
3 --> Sb
4 --> Sbc
5 --> Sc
7 --> Sd
8 --> Im etc..

- For the "shallow" approach we will use measurements from the [catalog provided](Nair_Abraham_cat.fit). It includes for every galaxy, strucutural parameters (sizes etc..), colors , SFRs and other indicators. 

- For the "deep" approach, the input will be the jpeg images. The jpeg images can be donwnloaded [here](https://drive.google.com/drive/folders/1ufj6ATroZ3emBbSQfQhcL_6W87EPgTaS?usp=sharing). The name is  matched to the ID in the catalog. Donwloand the tarball, save in folder IAC_XXX_WINTER/morphology and untar

- A [jupyter notebook](morph_classical_ML.ipynb) for the shallow approach is provided. I used RFs and ANNs.

- A [jupyter notebook](Nair_Sab_deep.ipynb) for the deep approach. CNN with a couple of layers.

