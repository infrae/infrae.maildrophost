# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from setuptools import setup, find_packages

name = "infrae.maildrophost"
version = "2.3dev"

setup(name = name,
      version = version,
      author = "Sylvain Viollon",
      author_email = "info@infrae.com",
      description = "Buildout recipe to install and setup maildrophost server",
      long_description = open('README.txt').read() + \
          open('docs/HISTORY.txt').read(),
      license = "ZPL 2.1",
      keywords = "maildrophost buildout",
      classifiers = ["Framework :: Buildout",
                     ],
      url = 'http://www.python.org/pypi/' + name,
      packages = find_packages(),
      namespace_packages = ['infrae'],
      install_requires = [
        'zc.buildout',
        'zc.recipe.egg',
        'setuptools',
        'psutil'],
      entry_points = {
        'zc.buildout':
            ['default = %s:Recipe' % name]},
    )
