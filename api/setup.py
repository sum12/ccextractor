from distutils.core import setup,Extension
from setuptools.command.develop import develop
from setuptools.command.install import install
import subprocess

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        subprocess.check_call(['./build_library'])
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        subprocess.check_call(['./build_library'])
        install.run(self)

setup(
       name='ccextractor',
       version = '0.1',
       author      = "Skrill",
       description = "Testing setup script for generating the module",
       cmdclass={
           'develop': PostDevelopCommand,
           'install':PostInstallCommand,
           },
       )
