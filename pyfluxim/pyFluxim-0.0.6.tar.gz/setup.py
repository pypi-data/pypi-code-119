from setuptools import setup, find_packages
import re

def description():
    with open('README.md') as f:
        return f.read()

def find_version():
    with open("pyFluxim/__init__.py",'r') as fp:
        src = fp.read()
        version_match = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]", src, re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find vesrion string.")
setup(
    name="pyFluxim",
    version=find_version(),
    description="library to handle data generated by Fluxim's hardwares",
    long_description=description(),
    long_description_content_type="text/markdown",
    url="https://github.com/fluxim/pyFluxim",
    author = "Olivier Scholder",
    author_email = "olivier.scholder@fluxim.com",
    license="Apache 2.0",
    keywords='fluxim litos lite phelos paios characterization suit',
    packages=find_packages(exclude=[]),
    package_data={},
    include_package_data=False,
    entry_points = {
        'console_scripts' : [],
        'gui_scripts':[]
    },
    install_requires=['numpy','matplotlib','h5py'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
