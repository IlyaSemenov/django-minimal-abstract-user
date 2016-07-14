# coding=utf-8
from distutils.core import setup
from setuptools import setup, find_packages

"""
Django AbstractUser without username, first_name, last_name, email but with is_staff and PermissionsMixin
"""

setup(
	name='django-minimal-abstract-user',
	version='0.0.2',
	url='https://github.com/IlyaSemenov/django-minimal-abstract-user',
	license='BSD',
	author='Ilya Semenov',
	author_email='ilya@semenov.co',
	description=__doc__,
	long_description=open('README.rst').read(),
	packages=['django_minimal_abstract_user'],
	install_requires=['Django>=1.8', 'django_abstract_utils==0.0.1'],
	classifiers=[],
)
