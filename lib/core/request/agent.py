import random
import string
import asyncio
import requests

def generate_user_agent():
    browser = random.choice(["Chrome", "Firefox", "Safari", "Edge"])
    version = ".".join([str(random.randint(1, 15)) for _ in range(3)])
    platform = random.choice(["Windows", "Macintosh", "Linux"])
    user_agent = f"{browser}/{version} ({platform}; { generate_random_string(10)})"
    return user_agent

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_user_agent_headers(num_headers):
    user_agent_headers = []
    for _ in range(num_headers):
        user_agent =  generate_user_agent()
        user_agent_headers.append({"User-Agent": user_agent})
    return user_agent_headers

def Prepare_the_headers():
    user_agent_headers =  generate_user_agent_headers(100)
    headers = []
    for header in user_agent_headers:
        headers.append(header["User-Agent"])
    return headers

headers = Prepare_the_headers()

# Usage with requests
url = "https://www.google.com"
payload = {"key1": "value1", "key2": "value2"}

headers_sqlgo = []

for header in headers:
    headers_sqlgo.append(header)