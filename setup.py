from setuptools import setup
import re, os


def find_packages(path='.'):
    ret = []
    for root, dirs, files in os.walk(path):
        if '__init__.py' in files:
            ret.append(re.sub('^[^A-z0-9_]+', '', root.replace('/', '.')))
    return ret


setup(name='toolbox',
      description='machine learning tools',
      version='0.0.1',
      author='Seho Kim',
      url='https://github.com/sehokim88/customtools',
      packages=find_packages(),
      install_requires=['numpy', 'pandas']
)
