# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'django-ubigeo-peru',
    version = '0.1',
    url = 'https://github.com/mickymiseck/django-ubigeo-peru',
    license = 'GPL v.3',
    description = 'Django app para aplicaciones que requieran usar los ubigeos del Perú.',

    long_description = read('README.md'),

    author = 'Miguel Angel Cumpa Asuña',
    author_email = 'themiseck.rock@gmail.com',

    packages = find_packages(),
    package_dir = {'': 'ubigeo'},
    exclude_package_data = { '': ['persona',] },

    install_requires = ['setuptools'],

    classifiers = [
        'Development Status :: Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL v.3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    include_package_data=True,
    zip_safe=False,
)
