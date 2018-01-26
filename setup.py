#!/usr/bin/env python
from setuptools import setup

setup(
    name='kodimock',
    version='0.0.3',
    description='Kodi modules code auto-completion and quick help for Python IDEs.',
    keywords='kodi plugin addon cli',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Software Development'],
    url='https://github.com/willforde/kodi-mock',
    author='william Forde',
    author_email='willforde@gmail.com',
    install_requires=['addondev'],
    license='MIT License',
    platforms=['OS Independent'],
    py_modules=['xbmc', 'xbmcaddon', 'xbmcgui', 'xbmcplugin', 'xbmcvfs'],
    include_package_data=True,
    zip_safe=False
)
