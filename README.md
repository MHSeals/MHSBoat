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

The scripts aren't entire functional at this point, so any help is useful.

In order to do PRs/commits, you can run the following commands (be sure to replace the blanks with your GitHub account info):

```bash
# Get access to the organization
sudo apt install gh -y
gh auth login
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Clone the repo
git clone https://github.com/MHSeals/MHSBoat.git
```

Now, in VS Code, you should have the ability to use the source control tab on the left to commit and sync changes that you make. Be sure to pull any changes before you start working to avoid conflicting branches. If you are using a different editor, you can look use git commands in your terminal (be sure to cd into the MHSBoat folder).

To run and test the script, cd into the MHSBoat folder and run:

```bash
colcon build
source install/setup.sh
ros2 launch mhsboat boat.launch.py
```

If there are any errors, you should try to fix them before doing a PR or commiting. Ask for help if needed.

The general structure of our project involves importing the scripts containing the functions for completing each task into our boat state machine and running it when our boat is in the appropriate state. 

**boat_state.py**
```python
from task1 import start_task1

def task1_state():
    start_task1()
```

**start_task1.py**
```python
import numpy as np
from utils import *

def start_task1():
    # Put the code including subscribers, publishers, nodes, etc. to complete the task
```
