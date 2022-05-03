from setuptools import setup, find_packages

setup(
    name="ODtools",
    version="2.1.13",
    author="zkrPython",
    author_email="178031608@qq.com",
    description="zkrTools",
    long_description="",
    license="Apache License",
    url="https://github.com/zkr-origin-data-dpt/ODtools",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        "xlrd",
        "xlwt",
        "redis==2.10.6",
        "elasticsearch==6.1.1",
        "thrift",
        "kafka-python",
        "redis-py-cluster==1.3.6",
        "pymysql",
        "loguru",
        "colorlog",
        "aiohttp==3.1.3",
        "aiosocksy==0.1.2",
        "apscheduler",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
