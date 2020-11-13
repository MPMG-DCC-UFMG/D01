from os import path

import setuptools

# Read the contents of your README file
# this_directory = path.abspath(path.dirname(__file__))
# with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
#     long_description = f.read()

setuptools.setup(
    name="casamento_entidade",
    version="0.1",
    author="Christian Gomes",
    author_email="christianrfg@gmail.com",
    description="MPMG M05 - Casamento de Entidades",
    long_description="Casamento de entidade utilizando Dedupe",
    long_description_content_type="text/markdown",
    url="https://github.com/christianrfg/m05",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: Ubuntu 18.04",
    ],
)
