from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="BiomarkersNIBC",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,  # Automatically install requirements
)