from setuptools import setup, find_packages

# Read the contents of the README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    author='Group2',
    description='CustomerFrequencyAnalysis',
    name='CustomerFrequency',
    version='0.1.0',
    packages=find_packages(include=['CustomerFrequency', 'CustomerFrequency.*']),
    long_description=long_description,
    long_description_content_type='text/markdown'
)

