from setuptools import setup
from setuptools import find_packages


VERSION = '0.1.7'

setup(
    name='StructEngPy', 
    version=VERSION, 
    author='Zhuoju Huang',
    author_email='zhuoju36@hotmail.com',
    license='MIT',
    description='package for structural engineering', 
    packages=find_packages(),
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=[
        'numpy>=1.21',
        'scipy>=1.7',
        'quadpy==0.16.1',
        'mpmath==1.2.1',
    ],
)