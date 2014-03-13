import sys
import os
import codecs

from setuptools import setup, find_packages


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

VERSION = "dev"

with codecs.open('README.rst', encoding='utf-8') as f:
    README = f.read()

setup(
    name='glanerbeard',
    version=VERSION,
    author='Daniele Sluijters, Rembrand van Lakwijk',
    author_email='github@daenney.net, rem@lakwijk.com',
    packages=find_packages(),
    url='https://github.com/daenney/glanerbeard',
    license='Apache License 2.0',
    description='Bridge multiple Sickbeards into one interface',
    include_package_data=True,
    long_description=README,
    install_requires=[
        "Flask >= 0.10.1",
        "requests >= 2.2.1",
        ],
    keywords="sickbeard glanerbeard",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        ],
)
