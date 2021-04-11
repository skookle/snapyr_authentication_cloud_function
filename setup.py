import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Don't import snapy module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'snapyr'))

long_description = '''Snapyr Python SDK'''

install_requires = [
    "requests>=2.7,<3.0",
    "six>=1.5",
    "monotonic>=1.5",
    "backoff==1.10.0",
    "python-dateutil>2.1"
]

tests_require = [
    "mock==2.0.0",
    "pylint==1.9.3",
    "flake8==3.7.9",
    "coverage==4.5.4"
]

setup(
    name='snapyr-python',
    url='https://github.com/snapyrautomation/snapyr-python',
    author='Segment',
    author_email='guests@snapyr.com',
    maintainer='Segment',
    maintainer_email='guests@snapyr.com',
    packages=['snapyr'],
    license='MIT License',
    install_requires=install_requires,
    extras_require={
        'test': tests_require
    },
    description='Snapyr',
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
