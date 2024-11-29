# Boat Scripts

This is still a work in progress. I am trying to experiment with the boat's configuration to make it easier to develop with. All you have to do to work with this repo is clone it into an empty workspace, install dependencies by running,

```bash
chmod +x install_dependencies.sh
sudo ./install_dependencies.sh
```

and to test the scripts, run.

```bash
colcon build
source install/setup.bash
ros2 launch mhsboat boat.launch.py
```

The scripts aren't entire functional at this point, so any help is wonderful.