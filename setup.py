from setuptools import setup, find_packages

setup(
    name='furniture-removal',
    version='0.0.0',
    author='fmintus',
    description='furniture-removal',
    packages = find_packages(exclude=("tests*")),
)