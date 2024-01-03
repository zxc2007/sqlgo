import urllib.parse
def get_url_part(url):
  o = urllib.parse.urlparse(url)
  url_part = o.scheme + "://" + o.netloc + o.path

  return url_part

# print(get_url_part("http://testfire.net/index.jsp?content=business_deposit.htm"))