from setuptools import setup, find_packages
import sys
import os
import pip


name = 'gtrans'
version = '0.0.1'
description = 'google translation command'
author = ''
author_email = ''
url = ''


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


install_requires = parse_requirements('requirements.txt')
reqs = install_requires

print(find_packages(exclude=['ez_setup', 'examples', 'tests']))
setup(name=name,
      version=version,
      description=description,
      long_description="""\
""",
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author=author,
      author_email=author_email,
      url=url,
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      test_suite='',
      entry_points={
          'console_scripts': ['gtrans=gtrans.gtrans:main']
      },
      )
