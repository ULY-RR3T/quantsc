from setuptools import setup

setup(
    name='quantsc',
    version='1.0.1',
    packages=['quantsc', 'quantsc.core', 'quantsc.data', 'quantsc.data.__random'],
    url='https://quantsc.org/',
    license='MIT',
    author='Yuanhao Lu, Jonathan Qin, Aditya Prasad ',
    author_email='terryl@usc.edu',
    description='A Quantitative Finance Library',
    install_requires=[
       'setuptools~=56.0.0',
       'pandas~=1.4.0',
        'numpy~=1.22.2',
        'yfinance=0.1.70',
        'statsmodels=0.13.2',
        'scipy~=1.8.0',
        'matplotlib~=3.5.1',
        'plotly~=5.7.0',
        'python-dateutil~=2.8.2',
        'yahoo_fin=0.8.9.1'
    ]
)
