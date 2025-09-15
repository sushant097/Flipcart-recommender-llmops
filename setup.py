from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Flipkart_recommender_system",
    version="0.1.0",
    author="Sushant",
    packages=find_packages(),
    install_requires=requirements,
)