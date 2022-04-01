import sys
from os.path import abspath, dirname, join

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


PY3 = sys.version_info > (3,)

VERSION = None
version_file = join(dirname(abspath(__file__)), 'src', 'SeleniumHelperLibrary', 'version.py')
with open(version_file) as file:
    code = compile(file.read(), version_file, 'exec')
    exec(code)

DESCRIPTION = """
Helper keywords for robotframework-selenium
"""[1:-1] 

CLASSIFIERS = """
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]


setup(
      name='robotframework-seleniumhelperlibrary',
      version=VERSION,
      description='Helper keywords for robotframework-selenium',
      long_description=DESCRIPTION,
      author='Shiva Adirala',
      author_email='adiralashiva8@gmail.com',
      url='https://github.com/adiralashiva8/robotframework-seleniumhelperlibrary',
      license='MIT',
      keywords='Helper keywords for robotframework-selenium',
      platforms='any',
      classifiers=CLASSIFIERS.splitlines(),
      package_dir={'': 'src'},
      packages=['SeleniumHelperLibrary'],
      install_requires=[
          'robotframework',
          'robotframework-seleniumlibrary'
      ],)