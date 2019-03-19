# Tutorial Sessions - Intelligence artificielle pour l'astrophysique à l'époque du big-data - ED127

_Authors: Alexandre Boucaud & Marc Huertas-Company_

These pages contain all the required information to run the tutorials. Please follow the instructions below to set up ypur environment.

### Set up your environment

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



