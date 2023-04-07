from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

VERSION = '0.1.21'
DESCRIPTION = 'A Python library for mathematical finance.'

# Setting up
setup(
    name="QFin",
    license='MIT',
    version=VERSION,
    author="Roman Paolucci",
    author_email="<romanmichaelpaolucci@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['scipy', 'numpy'],
    keywords=['python', 'finance'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

# python setup.py sdist bdist_wheel
# twine upload dist/*
