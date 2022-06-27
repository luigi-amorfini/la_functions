from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='la_functions',
      version='0.1.0',
      description='Luigi Amorfini My Library Functions - la_functions',
      long_description=readme(),
      license='GPL',
      author='Luigi Amorfini',
      author_email='amorfiniluigi82@gmail.com',
      url='#',
      packages=['la_functions'],
)
