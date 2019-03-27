from setuptools import setup
setup(name='toolbox',
      description='machine learning tools',
      version='0.0.1',
      author='Seho Kim',
      url='https://github.com/sehokim88/customtools',
      packages=['toolbox', 'preprocessing', 'pipelining', 'modeling', 'scoring'],
      install_requires=['numpy', 'pandas']
)
