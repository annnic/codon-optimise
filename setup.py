import os

from setuptools import find_packages, setup

install_requires = [
    line.rstrip()
    for line in open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
]

setup(
    name="codon-optimise",
    install_requires=install_requires,
    version="0.0.1",
    description="Optimising codons for P. pacificus CUB 10 and 3",
    url="https://github.com/annnic/codon-optimise",
    license="MIT",
    packages=find_packages(),
    zip_safe=False,
)