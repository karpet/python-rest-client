"""
    Copyright (C) 2011 Ben James

    This file is part of python-fedoracommons.

    python-fedoracommons is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    python-fedoracommons is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with python-fedoracommons.  If not, see <http://www.gnu.org/licenses/>.
"""

__license__ = 'GPL http://www.gnu.org/licenses/gpl.txt'
__author__ = "Ben James <benj@lshift.net>"
__version__ = '0.1'

from distutils.core import setup

setup(name='python-rest-client',
      version='0.1',
      author="Benjamin O'Steen",
      author_email='bosteen@gmail.com',
      py_modules=['gae_restful_lib', 'microblog_exceptions', 'mimeTypes', 'restful_lib', 'talis', 'tinyurl', 'twitter'],
      packages=['httplib2']
      )
