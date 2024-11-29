#!/usr/bin/env bash

# Detect if NVIDIA graphics are being used
if lspci | grep -i nvidia > /dev/null; then
    pip3 install torchaudio
elif lspci | grep -i "vga.*intel" > /dev/null || lspci | grep -i "vga.*amd" > /dev/null; then
    pip3 install torchaudio --index-url https://download.pytorch.org/whl/cpu
else
    echo "No compatible graphics detected."
fi

# Uninstall conflicting OpenCV versions
pip3 uninstall -y opencv-contrib-python opencv-python-headless opencv-contrib-python-headless

# Install necessary Python dependencies
pip3 install pyyaml matplotlib scikit-learn ultralytics torch torchvision opencv-python

sudo apt -y install \
ros-humble-velodyne_driver