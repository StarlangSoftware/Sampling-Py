from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='nlptoolkit_sampling',
    version='1.0.8',
    packages=['Sampling'],
    url='https://github.com/StarlangSoftware/Sampling-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Data sampling library',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
