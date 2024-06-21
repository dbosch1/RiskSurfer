from setuptools import setup, find_packages

setup(
    name='RiskSurfer',
    version='0.1',
    packages=find_packages(include=['risksurfer', 'risksurfer.*']),
    install_requires=[
        'yfinance',
        'pandas',
        'numpy',
        'matplotlib',
    ],
    author='Paula Palermo, Eitan Razuri Olazo, Daniele Boschetti',
    description='A Python package for stock data fetching, risk analysis, and visualization.',
    url='https://github.com/dbosch1/RiskSurfer',
)
