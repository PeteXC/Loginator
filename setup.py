from setuptools import setup
from setuptools import find_packages
from io import open
from os import path
import os
import loginator
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

### REQUIREMENTS ###
# automatically captured required modules for install_requires in requirements.txt
if path.exists(path.join(HERE, "requirements.txt")):
    with open(path.join(HERE, "requirements.txt"), encoding="utf-8") as f:
        all_reqs = f.read().split("\n")
else:
    with open(path.join(HERE, "loginator.egg-info/requires.txt"), encoding="utf-8") as f:
        all_reqs = f.read().split("\n")

INSTALL_REQUIRES = [
    x.strip() for x in all_reqs if ("git+" not in x) and (not x.startswith("#")) and (not x.startswith("-"))
]
dependency_links = [x.strip().replace("git+", "") for x in all_reqs if "git+" not in x]

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="loginator",
    version="0.0.16",
    author="Peter Chai",
    author_email="peterchai2008@hotmail.co.uk",
    description="A rudimentary command line tool to help you download logs and other files from S3",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="logs aws loginator aws-s3 s3 bucket",
    options={"bdist_wheel": {"universal": True}},
    url="https://github.com/PeteXC/Loginator",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    package_data={'': ['requirements.txt', ]},
    include_package_data=True,
    entry_points={
        "console_scripts": ["loginator=loginator.loginator:run"],
    },
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.6",
)
