# -*- coding: utf-8 -*-
import sys
from distutils.core import setup, Extension

USE_CYTHON = True

SOURCE_EXT = '.pyx' if USE_CYTHON else '.cpp'
EXT_MODULES = [Extension(
    'pugixmltodict',
    sources=[
        'pugixmltodict' + SOURCE_EXT,
        'pugixml/src/pugixml.cpp',
    ],
)]

if USE_CYTHON:
    from Cython.Build import cythonize
    EXT_MODULES = cythonize(EXT_MODULES)


setup(
    name='pugixmltodict',
    version='0.5',
    description='A fast alternative to xmltodict library',
    url='https://github.com/sepeth/pugixmltodict',
    author='Doğan Çeçen',
    author_email='sepeth@gmail.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        'Topic :: Text Processing :: Markup :: XML',
    ],
    setup_requires=['cython>=0.24.1'],
    install_requires=['cython>=0.24.1'],
    ext_modules=EXT_MODULES,
)
