# CMAKE 3.24 on Ubuntu 22.04 

This file contains step by step guide to install cmake 3.24 onn ubuntu
Below are the commands to install cmake

## Step 1: Remove Older Versions of CMake
First, check if an older version of CMake is already installed:

```bash
cmake --version
```
If it’s an older version and you want to remove it, run:

```bash
sudo apt remove --purge cmake
```
## Step 2: Install Required Dependencies
Ensure the required tools for building CMake are installed:

```bash
sudo apt update
sudo apt install -y build-essential libssl-dev
```
## Step 3: Download the CMake Source Code
Download the source code for CMake 3.24 from its official website or use wget:

```bash
wget https://github.com/Kitware/CMake/releases/download/v3.24.0/cmake-3.24.0.tar.gz
```
Extract the downloaded file:

```bash
tar -zxvf cmake-3.24.0.tar.gz
cd cmake-3.24.0
```
## Step 4: Build and Install CMake
Build CMake from source:

```bash
./bootstrap
make
sudo make install
```

## Step 5: Verify Installation
After installation, verify the installed version:

```bash
Copy code
cmake --version
```
You should see CMake 3.24 as the installed version.

