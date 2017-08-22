"""

setup.py file for SWIG example
"""

from distutils.core import setup,Extension
from setuptools.command.develop import develop
from setuptools.command.install import install
import os
import subprocess

def generate_source_list():
    original = os.getcwd()
    os.chdir("../src")
    source_code = {}
    source = ['../src/ccextractor.c']
    for root,dirs, files in os.walk(os.getcwd()):
        if root != os.getcwd():
            modded_root = os.path.relpath(root,original)
            source_code[modded_root] = [f for f in os.listdir(root) if f.endswith(".c")]
    os.chdir("../api")
    root = os.getcwd()
    modded_root = os.path.relpath(root,original)
    source_code[modded_root] = [f for f in os.listdir(root) if f.endswith(".c")]
    for root,dirs, files in os.walk(os.getcwd()):
        if root != os.getcwd() and ".venv" not in root and "build" not in root:
            modded_root = os.path.relpath(root,original)
            source_code[modded_root] = [f for f in os.listdir(root) if f.endswith(".c")]
    for item in source_code.keys():
            for each in source_code[item]:
                source.append(os.path.join(item, each))
    return source

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        subprocess.call(['./build_library'])
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        subprocess.call(['./build_library'])
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
""""
source = generate_source_list()
BLD_INCLUDE=['/usr/include/python2.7/','../src','/usr/include/leptonica/','/usr/include/tesseract/','../src/lib_ccx/','../src/gpacmp4/','../src/libpng/','../src/zlib/','../src/zvbi','../src/lib_hash','-../src/protobuf-c','../src/utf8proc']
BLD_LINKER=['m','zmuldefs','tesseract','lept','python2.7']
ccextractor_module = Extension('_ccextractor',
                           sources=source,
                           include_dirs = BLD_INCLUDE,
                           define_macros=[('PYTHONAPI','1')],
                           libraries=BLD_LINKER,
                           )

setup (name = 'ccextractor',
       version = '0.1',
       author      = "Skrill",
       description = "Testing setup script for generating the module",
       ext_modules = [ccextractor_module],
       py_modules = ["ccextractor"],
       )
"""
