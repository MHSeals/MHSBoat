#!/usr/bin/env bash

: '

NOTE: To run this script, use the following commands
after entering to the directory that contains it
chmod +x install_dependencies.sh
sudo ./install_dependencies.sh

  '

sudo pip3 install --upgrade pip

# Detect if NVIDIA graphics are being used
if lspci | grep -i nvidia > /dev/null; then
    pip3 install torchaudio
elif lspci | grep -i "vga.*intel" > /dev/null || lspci | grep -i "vga.*amd" > /dev/null; then
    pip3 install torchaudio --index-url https://download.pytorch.org/whl/cpu
else
    echo "No compatible graphics detected."
fi

# Uninstall conflicting OpenCV versions
pip3 uninstall -y opencv-contrib-python opencv-python-headless opencv-contrib-python-headless numpy

# Install necessary Python dependencies
pip3 install pyyaml matplotlib scikit-learn ultralytics torch torchvision opencv-python
pip3 install numpy==1.26.1
pip3 install pygame

# Install necessary ROS2 Humble packages
sudo apt -y install \
ros-humble-velodyne-driver \
ros-humble-cv-bridge \
ros-humble-rosidl-default-generators \
ros-humble-rosidl-default-runtime