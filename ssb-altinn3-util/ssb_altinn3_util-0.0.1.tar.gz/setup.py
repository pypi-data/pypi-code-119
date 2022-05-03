import setuptools

with open("README.md", "r",) as fh:
    long_description = fh.read()

setuptools.setup(
    name="ssb_altinn3_util",
    version="0.0.1",
    author="Team Cumulus",
    author_email="nhk@ssb.no, lrb@ssb.no, gij@ssb.no, kuv@ssb.no",
    description="A small library package containing various tools and utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/statisticsnorway/altinn3-common-util",
    project_urls={
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        'google-cloud-pubsub',
        'google-cloud-secret-manager'
    ],

    python_requires=">=3.6",
)
