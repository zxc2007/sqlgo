import urllib.parse
import requests
import re


def update_url(url,value):
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)

    param_names = re.findall(r'[\?&]([^&=]+)=', url)

    for param_name in param_names:
        query_params[param_name] = value 

    new_query_string = urllib.parse.urlencode(query_params, doseq=True)
    new_url = urllib.parse.urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, new_query_string, parsed_url.fragment))
    return new_url

# url = "https://example.com/api?id=value1&param2=value2"
# new_url = update_url(url,"OR 1=1")
# print(new_url)