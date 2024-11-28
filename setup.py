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
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    author="Martin High School",
    description="MHSeals Boat Scripts",
    license="GNU GPLv3",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "mhsboat = mhsboat.run:main"
        ],
    },
)