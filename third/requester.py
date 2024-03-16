#!/usr/bin/env python
"""
# SQLGO License - Version 1.4

Copyright (C) 2023-2024 Heisenberg

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
import urllib
try:
    import urllib2
except:
    pass

# post_request.py

class PostRequest:
    def __init__(self, url, data=None, session=None):
        self.url = url
        self.data = data
        self.session = session

    def send(self):
        if self.data:
            self.data = urllib.urlencode(self.data)
        if self.session:
            response = self.session.post(self.url, self.data)
        else:
            response = urllib2.urlopen(self.url, self.data)
        self.response = response.read()
        return self

    @property
    def text(self):
        return self.response.decode('utf-8')
# get_request.py

class GetRequest:
    def __init__(self, url, params=None, session=None):
        self.url = url
        self.params = params
        self.session = session

    def send(self):
        if self.params:
            self.url = '{}?{}'.format(self.url, urllib.urlencode(self.params))
        if self.session:
            response = self.session.get(self.url)
        else:
            response = urllib2.urlopen(self.url)
        self.response = response.read()
        return self

    @property
    def text(self):
        return self.response.decode('utf-8')

def get(url, params=None,*args,**kwargs):
    return GetRequest(url, params).send().text
def post(url, data=None,*args,**kwargs):
    return PostRequest(url, data).send().text

def session():
    pass