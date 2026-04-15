# setup.py is the standard build script for setuptools-based Python projects.
#
# It defines metadata, dependencies, and installation behavior for the package.
# For example, it can specify the package name, version, author, required libraries,
# and which modules should be included when the project is installed.
#
# When someone runs `pip install .` or `python setup.py install`, this file is used
# to tell Python packaging tools how to build and install the package correctly.
#
# Even if this file is currently empty, its typical importance is:
# - packaging the code for distribution
# - installing dependencies automatically
# - registering console scripts or entry points
# - defining package metadata for PyPI
#
# If you want this repository to be installable, you should add a setuptools-based
# setup() call here or use a modern alternative like pyproject.toml.


from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:

    requirement_lst: List[str] = []
    """Read the requirements from the requirements.txt file."""
    try:
        with open('requirements.txt') as f:
            lines= f.readlines()
            for line in lines:
                requirement= line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

print(get_requirements())    

setup(
    name='NetworkSecurity',
    version='0.1.0',
    packages=find_packages(),
    install_requires=get_requirements(),
    author='Hamza'
)