from setuptools import setup, find_packages

setup(
    name="bengine",
    version="1.0.0",
    description="The best game engine.",
    author="slugnasty",
    keywords="bengine",
    packages=find_packages(),
    install_requires=["glfw", "PyOpenGL", "numpy"]
)