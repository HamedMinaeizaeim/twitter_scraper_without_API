from setuptools import setup
import setuptools
import os
import sys

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = [] # Here we'll get: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirementPath):
    with open(requirementPath,encoding='utf-8') as f:
        install_requires = f.read().splitlines()

print(install_requires)
setup(
    name='twitter_scraper_without_api',
    version='0.0.5',
    license='',
    author='Hamed',
    author_email='hamed.minaei@gmail.com',
    description='twitter_scraper without API',
    long_description=read_file('README.MD'),
    long_description_content_type="text/markdown",
    url="https://github.com/HamedMinaeizaeim/twitter_scraper",
    project_urls={
        "Bug Tracker": "https://github.com/HamedMinaeizaeim/twitter_scraper/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    packages=['twitter_scraper_without_api'],
    package_dir={'': 'src'},
    python_requires=">=3.6",
)
