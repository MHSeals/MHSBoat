import os
from glob import glob
from setuptools import find_packages, setup

package_name = "mhsboat"

setup(
    name=package_name,
    version="0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*'))),
        (os.path.join('share', package_name, 'data'), glob(os.path.join('data', '*'))),
        (os.path.join('share', package_name, 'msgs'), glob(os.path.join('msgs', '*.msg'))),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    author="Martin High School",
    description="MHSeals Boat Scripts",
    license="GNU GPLv3",
    tests_require=["pytest"],
    entry_points={ # All scripts that run standalone should be here if run through the launch file
        'console_scripts': [
            'boat_state = mhsboat.boat_state:main',
            'motors = mhsboat.motors:main',
            'yolo = mhsboat.sensors.yolo:main',
        ],
    }
)