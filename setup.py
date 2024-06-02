# install src as local package

from setuptools import find_packages, setup

setup(
    name = "Generative AI project",
    version = "0.0.0",
    author = "Pritha Tyagi",
    author_email= "tyagipri1@gmail.com",
    packages= find_packages(), # automatically find constructor i.e. __init__.py file
    install_requires = [] #

)