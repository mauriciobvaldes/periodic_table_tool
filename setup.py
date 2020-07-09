from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='periodictool',
    version='1.0',
    description='This program will let you search the periodic table',
    long_description=readme,
    author='Mauricio Böckin',
    author_email='mbockin@kth.se',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
