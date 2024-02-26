# post_request.py
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