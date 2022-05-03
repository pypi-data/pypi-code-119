from setuptools import setup, find_packages


setup(
    name='exergenicslayers',
    version='1.4',
    author="Sanjeevani Avasthi",
    author_email='sanjeevani.avasthi@exergenics.com',
    packages=['exergenicslayers'],
    # package_dir={'': 'src'},
    url='https://github.com/Exergenics/internal-portal-api-lambda',
    keywords='exergenics portal layer api',
    install_requires=[
          'boto3',
          'datetime',
          'requests',
          'urllib3'
      ],
)
