#!/usr/bin/env python

from setuptools import setup, find_packages
import glob

setup(name='examplepackage',
      description='Example package',
      long_description='Example package',
      url='https://github.com/markM2864/python-deb.git',
      author='Me',
      author_email='my@email.com',
      maintainer='Me',
      maintainer_email='my@email.com',
      license='MIT',
      packages=find_packages(),
      scripts=['bin/examplepackage','examplepackage-run.py'],
      data_files=[('share/examplepackage', ['share/examplepackage.png']),
                  ('share/examplepackage', ['share/examplepackage.desktop']),
                  ('share/examplepackage', ['share/polkit/local.examplepackage.policy'])],
      install_requires=[""],
      zip_safe=False)