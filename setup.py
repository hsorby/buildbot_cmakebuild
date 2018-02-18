
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'buildbot_cmakebuild', 'version.txt'), encoding='utf-8') as f:
    version = f.read()

print('"%s"' % version)

setup(
    name='buildbot_cmakebuild',
    version=version,
    description='A Buildbot plugin build step for building CMake-based projects.',
    long_description=long_description,
    url='https://github.com/hsorby/buildbot_cmakebuild',
    keywords='buildbot buildbot-plugin',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['buildbot>=0.9.1'],
    package_data={
        'buildbot_cmakebuild': ['version.txt'],
    },
    entry_points={
        'buildbot.steps': [
            'CMakeBuild = buildbot_cmakebuild.cmakebuild:CMakeBuild'
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache 2.0 License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)