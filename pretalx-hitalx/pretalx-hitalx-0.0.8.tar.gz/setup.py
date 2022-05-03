import os
from distutils.command.build import build

from django.core import management
from setuptools import find_packages, setup

try:
    with open(
        os.path.join(os.path.dirname(__file__), "README.rst"), encoding="utf-8"
    ) as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""


class CustomBuild(build):
    def run(self):
        management.call_command("compilemessages", verbosity=1)
        build.run(self)


cmdclass = {"build": CustomBuild}


setup(
    name="pretalx-hitalx",
    version="0.0.8",
    description="Some utilities specifically for the Hedonist International",
    long_description=long_description,
    url="https://github.com/l0rn/pretalx-hitlax",
    author="Jonatan Zint",
    author_email="j.zint@frykk.de",
    license="Apache Software License",
    install_requires=[
        'django-autocomplete-light'
    ],
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretalx.plugin]
pretalx_hitalx=pretalx_hitalx:PretalxPluginMeta
""",
)
