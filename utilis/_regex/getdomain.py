import re
import socket

def extract_domain(url):
    pattern = re.compile(r'https?://(?:www\.)?([^/]+)') if "https" in url else re.compile(r'https?://(?:www\.)?([^/]+)')
    match = pattern.match(url)
    if match:
        return str(socket.gethostbyname(match.group(1)))
    else:
        return None

# print(extract_domain("https://scanme.org/"))