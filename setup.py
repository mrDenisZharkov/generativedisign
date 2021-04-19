import sys
import setuptools


INSTALL_REQUIRES = [
    'absl-py',
    'apache-beam',
    'autograd',
    'nlopt',
    'numpy',
    'matplotlib',
    'Pillow',
    'scipy',
    'scikit-image',
    'seaborn',
    'xarray',
]

if sys.version_info[:2] < (3, 7):
  INSTALL_REQUIRES.append('dataclasses')


setuptools.setup(
    name='neural-structural-optimization',
    version='0.0.0',
    license='Apache 2.0',
    author='Google LLC',
    author_email='noreply@google.com',
    install_requires=INSTALL_REQUIRES,
    url='https://github.com/mrDenisZharkov/generativedisign',
    packages=setuptools.find_packages(),
    python_requires='>=3.6')
