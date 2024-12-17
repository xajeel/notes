# Here are the steps to Install CUDA ( Any Version ) on Linux

## Step 01:

Go to the following link & select the GPU options.

Link: https://www.nvidia.com/en-us/drivers/

Download the `.deb` file and use `dpkg` 

```
dpkg -i [driver name]
```
Then install the driver 

```
sudo apt install nvidia-driver-[number]
```
[ number ] is mentioned in the name of the driver file ( .deb file ). Then update the system usiing 

```
sudo apt update
```
Then check the driver by using command 

```
nvidia-smi
```
If it runs then ok. If it does not run then reboot the device.

## Step Two

After `step 01` go the following page & select the relavent options

Link: https://developer.nvidia.com/cuda-toolkit-archive

then just copy paste the two commands & after doing it just check the cuda using 

```
nvcc --version 
```