# Tutorial Sessions - Intelligence artificielle pour l'astrophysique à l'époque du big-data - ED127

_Authors: Alexandre Boucaud & Marc Huertas-Company_

These pages contain all the required information to run the tutorials of the [course](https://github.com/mhuertascompany/deeplearning4astronomy). Please follow the instructions below to set up ypur environment.

### Set up your environment

1. clone this repository
  ```
  git clone https://github.com/aboucaud/deeplearning4astro_labs_2019.git
  cd deeplearning4astro_labs_2019
  ```
  
2. install the dependencies
  - with [conda](https://www.anaconda.com/download/) 
  This option is highly recommended to ensure that the installation will not interfere with your current python installation
  ```
  conda install -y -c conda conda-env     # First install conda-env
  conda env create                        # Use environment.yml to create the 'dl4astro19' env
  conda activate dl4astro19       # Activates the virtual env
  ```
  - without `conda` (best to use a virtual environment)
  ```
  python -m pip install -r requirements.txt
  ```

3. Only if your system has an Nvidia GPU (not for Mac)
 
 - check if the nvidia drivers are installed by typing nvidia-smi in a terminal. If the command is not recognized, download and install from here [https://www.nvidia.com/Download/index.aspx?lang=en-us]. You will need root access and the model of your GPU.
 
 - within your virtual environment type:
  ```
  conda install tensorflow-gpu cudatoolkit=9.0
   ```


