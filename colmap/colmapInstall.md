# This file contains step by step Instructions to install Colmap with CUDA on Linux System

## Note

if you have `gcc 11.x` on Ubuntu 22.04 then we need to run following commands 
```
sudo apt-get install gcc-10 g++-10
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 100
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-10 100
```

## Installation

- First install ninja build
```
sudo apt-get install ninja-build
```

- Second Install all the dependencies required for the colmap
```
sudo apt-get install -y \
    cmake \
    build-essential \
    libboost-program-options-dev \
    libboost-filesystem-dev \
    libboost-graph-dev \
    libboost-regex-dev \
    libboost-system-dev \
    libboost-test-dev \
    libeigen3-dev \
    libflann-dev \
    libfreeimage-dev \
    libmetis-dev \
    libgoogle-glog-dev \
    libgflags-dev \
    libsqlite3-dev \
    libglew-dev \
    qtbase5-dev \
    libqt5opengl5-dev \
    libcgal-dev \
    libcgal-qt5-dev \
    libsuitesparse-dev \
    libceres-dev
```

- Cloning the git hub repo of colmap and navigating to the directory 
```
git clone https://github.com/colmap/colmap.git
cd colmap
```

- Making a directory name `build`
```
mkdir build
cd build
```

- Running `cmake` command to build the colmap. We need to specify the GPU Archtecture [ I'm using A100 so its `80` ]
```
cmake .. -GNinja -DCMAKE_BUILD_TYPE=Release -DCUDA_ENABLED=ON -DCMAKE_CUDA_ARCHITECTURES= [ GPU Archtecture ]
```

- Then in the end we need to run the following teo commands 
```
ninja
sudo ninja install
```

## Running Colmap on Custom Dataset

- Below is the folder structure 
```
project_directory/
├── images/           # Folder with JPG images
├── colmap_output/    # Folder for database.db
```
- *Colmap Feature Extractor*
```
colmap feature_extractor --database_path colmapOutput/database.db --image_path jpgImages
```

- *Colmap Exhaustive Matcher*
```
colmap exhaustive_matcher --database_path colmapOutput/database.db
```

- *Colmap Mapper*
```
colmap mapper --database_path colmapOutput/database.db --image_path jpgImages --output_path colmapOutput/sparse
```