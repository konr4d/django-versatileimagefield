# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-versatileimagefield',
    packages=find_packages(),
    version='1.10.1',
    author=u'Jonathan Ellenberger',
    author_email='jonathan_ellenberger@wgbh.org',
    url='http://github.com/respondcreate/django-versatileimagefield/',
    license='MIT License, see LICENSE',
    description="A drop-in replacement for django's ImageField that provides "
                "a flexible, intuitive and easily-extensible interface for "
                "creating new images from the one assigned to the field.",
    long_description=open('README.rst').read(),
    zip_safe=False,
    install_requires=['Django>2', 'Pillow<7.0.0', 'six>1.10'],
    include_package_data=True,
    keywords=[
        'django',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Multimedia :: Graphics :: Presentation',
    ]
)
