# Deep learning tutorial for Astro PhDs

_Authors: Alexandre Boucaud & Marc Huertas-Company_

### Set up

1. clone this repository
  ```
  git clone https://github.com/aboucaud/deeplearning4astro_labs_2019.git
  cd deeplearning4astro_labs_2019
  ```
  
2. install the dependencies
  - with [conda](https://www.anaconda.com/download/)
  ```
  conda install -y -c conda conda-env     # First install conda-env
  conda env create                        # Use environment.yml to create the 'dl4astro19' env
  conda activate dl4astro19       # Activates the virtual env
  ```
  - without `conda` (best to use a virtual environment)
  ```
  python -m pip install -r requirements.txt
  ```

3. download the data
  ```
  python download_data.py        # quick-test data for testing ~16Mo
  python download_data.py full   # full dataset ~1.5Go
  ```

### New submissions

1. create a new submission "<new_sub>" by building on the existing ones
  ```
  mkdir submissions/<new_sub>
  cp submissions/keras_fcnn/object_detector.py submissions/<new_sub>/.
  ```
2. modify the file `submissions/<new_submission>/object_detector.py` with your favorite editor

3. test it with
  ```
  ramp_test_submission --quick-test --submission <new_sub>
  ```
4. if the job complete, you can submit the code in the sandbox of ramp.studio
  

### Local notebook

Get started on this RAMP with the [dedicated notebook](astrophd_tutorial_starting_kit.ipynb)

### Help

- Go to the `ramp-workflow` [wiki](https://github.com/paris-saclay-cds/ramp-workflow/wiki) for more help on the [RAMP](http:www.ramp.studio) ecosystem.
- Sign up on the [CDS Slack](cds-upsay.slack.com) and join the `#phd_tutorial` channel.


### Acknowledgements

We thank the CCIN2P3 for providing us with GPU time for the students to train their models during the whole week of the teaching course.

 [![CCIN2P3](img/logosimpleCC.jpg)](https://cc.in2p3.fr/en/)
