from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='tgming',
      version=version,
      description="TurboGears2 Support for Ming MongoDB ORM",
      long_description="""\
tgming is used by TurboGears2 to support ming backend. To create
a ming project just use quickstart command with --ming option
it will automatically setup tgming and all the required dependencies
""",
      classifiers=[
        "Environment :: Web Environment",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: TurboGears"
      ], 
      keywords='turbogears2.extension',
      author='Alessandro Molina',
      author_email='alessandro.molina@axant.it',
      url='http://bitbucket.org/_amol_/turbogears-ming',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "repoze.what >= 1.0.8",
        "repoze.who-friendlyform >= 1.0.4",
        "repoze.what-pylons >= 1.0",
        "repoze.who==1.0.19",
        "ming"
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
