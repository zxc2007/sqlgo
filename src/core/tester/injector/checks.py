#!/usr/bin/env python
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
import re
import os
import sys
try:

    import urllib.parse
except:
    import urlparse as urllib

from src.core.enums.devstatus import DevStatus
from src.core.enums.priority import PRIORITY

__status__ = DevStatus.READY_FOR_PRODUCTION_AND_USE
__priority__ = PRIORITY.NORMAL
def newline_fixation(payload):
    payload = urllib.parse.unquote(payload)
    if "\n" in payload:
        #_ = payload.find("\n") + 1
        #payload = _urllib.parse.quote(payload[:_]) + payload[_:]
        payload = payload.replace("\n","%0a")
    if "\r" in payload:
        #_ = payload.find("\r\n") + 1
        #payload = _urllib.parse.quote(payload[:_]) + payload[_:]
        payload = payload.replace("\r","%0d")
    return payload

import re
try:
    import requests
except:
    import third.requester as requests

def extract_sentence_with_error(html_content, error_word):
    # Define a regular expression to find sentences containing the error word
    sentence_pattern = re.compile(r'[^.!?]*\b' + re.escape(error_word) + r'\b[^.!?]*[.!?]', flags=re.IGNORECASE)

    # Find all matches in the HTML content
    sentence_matches = sentence_pattern.findall(html_content)

    # Return a random sentence (if any found)
    if sentence_matches:
        import random
        return random.choice(sentence_matches)
    else:
        return None


def extract_some_keyword(url):
# Make a request to a website (replace the URL with your target URL)
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200 or True:
        # Extract HTML content
        html_content = response.text

        # Define error word (replace with your target error word)
        error_word = "Error"

        # Extract a sentence containing the error word
        sentence_with_error = extract_sentence_with_error(html_content, error_word)
        return sentence_with_error

        # Print the result
    #     if sentence_with_error:
    #         print(f"Random sentence containing the error word '{error_word}':")
    #         print(sentence_with_error)
    #     else:
    #         print(f"No sentences found containing the error word '{error_word}'.")
    # else:
    #     print(f"Error: Unable to fetch URL. Status code: {response.status_code}")
