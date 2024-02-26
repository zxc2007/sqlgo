"""
# SQLGO License - Version 1.1

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
try:
    import urllib.parse
except:
    import urlparse as urllib

try:
    import requests
except:
    import third.requester as requests
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