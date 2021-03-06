"""Setup package"""

from setuptools import setup, find_packages # type: ignore

with open("readme.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name="python-izone",
    version="1.0.2",
    author="Penny Wood",
    author_email="pypl@ninjateaparty.com",
    description="A python interface to the iZone airconditioner controller",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/Swamp-Ig/pizone",
    install_requires=['aiohttp>=3.4', 'requests', 'netifaces'],
    tests_require=['aiounittest'],
    packages=find_packages(exclude=['tests', 'tests.*']),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ]
)
