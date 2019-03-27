from setuptools import setup, find_packages
setup(name='toolbox',
      description='machine learning tools',
      version='0.0.1',
      author='Seho Kim',
      url='https://github.com/sehokim88/customtools',
      package_dir = {
            'toolbox': 'toolbox',
            'toolbox.pipelining': 'toolbox.pipelining'},
      packages=['toolbox', 'toolbox.pipelining'],
      install_requires=['numpy', 'pandas']
)
