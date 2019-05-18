#!/usr/bin/env python

from setuptools import find_packages, setup
setup(name='Distutils',
      version='1.0',
      author='Matskiv Oksana',
      py_modules=['main'],
      # packages=['course_work'],
      scripts=['main.py'],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'police-api-client',
          'matplotlib',
          'numpy'
      ],
      )
