from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="azcam-cryocon",
    version="21.2.2",
    description="azcam extension for Cryo-con temperature controllers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Michael Lesser",
    author_email="mlesser@arizona.edu",
    keywords="",
    license=license,
    packages=find_packages(),
    zip_safe=False,
    url="https://mplesser.github.io/azcam/",
    install_requires=["azcam"],
)
