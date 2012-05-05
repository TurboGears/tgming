from setuptools import setup, find_packages
import sys, os

version = '0.0.5'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''

setup(name='tgming',
      version=version,
      description="TurboGears2 Support for Ming MongoDB ORM",
      long_description=README,
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
        "repoze.who-friendlyform >= 1.0.4",
        "repoze.who >= 1.0.19",
        "repoze.who-testutil >= 1.0.1",
        "ming"
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
