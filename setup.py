from setuptools import setup, find_packages
VERSION = '0.0.1'
DESCRIPTION = 'test'

# Setting up
setup(
    name="yolocrop",
    version=VERSION,
    author="seyed",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python<=5.0.0']
)