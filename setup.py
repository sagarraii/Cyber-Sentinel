'''
DESCRIPTION for setup.py

setup.py is a Python script used to package, distribute, and install a Python project.
It acts as the instruction manual that tells packaging tools how this project should be built and installed

When we create a Python project, our code sits in folders.
But Python doesn't automatically know:

1. what the package name is?
2. what version it is?
3. what dependencies it needs?
4. which folders contain installable code?

setup.py provides this metadata so the project can be installed like a real Python library.
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    requirement_lst:List[str]=[]

    try:
        with open ('requirements.txt', 'r') as file:
            # read line from the files
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

# Project MetaData

setup(
    name="Cyber Sentinel",
    version="0.0.1",
    author="Sagar Rai",
    author_email="sagarrai9547@gmail.com",
    description="Machine Learning System for detecting network threats",
    packages=find_packages(),
    install_requires=get_requirements()
)