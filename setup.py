from setuptools import setup, find_packages

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    author='Group2',
    description='CustomerFrequencyAnalysis',
    name='CustomerFrequency',
    version='0.1.0',
    packages=find_packages(include=['CustomerFrequency', 'CustomerFrequency.*']),
    long_description= long_description,
    long_description_content_type='text/markdown'

)


