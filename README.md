# Deep learning tutorial for Astro PhDs

_Authors: Alexandre Boucaud & Marc Huertas-Company_

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

3. download the data
  ```
  python download_data.py        # quick-test data for testing ~16Mo
  python download_data.py full   # full dataset ~1.5Go
  ```


