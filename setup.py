from setuptools import find_packages, setup

setup_requires = []

install_requires = [
        "pysdfgen"
]

setup(
    name="dummy",
    version="0.0.1",
    install_requires=install_requires,
    packages=find_packages(exclude=("tests", "docs"))
)
