import urllib.parse
def get_url_part(url):
    # Find the URL part (scheme:[//host[:port]][/]path)
    o = urllib.parse.urlparse(url)
    url_part = o.scheme + "://" + o.netloc + o.path

    return url_part