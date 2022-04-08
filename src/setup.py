from setuptools import setup

setup(
    name='sdig',
    version='0.1',
    description='Simple module for reading ERDDAP metadata',
    author='Roland Schweitzer',
    author_email='roland.schweitzer@noaa.gov',
    packages=['sdig'],  # same as name
    install_requires=['pandas'],  # external packages as dependencies
)