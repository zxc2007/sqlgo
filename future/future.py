from bs4 import BeautifulSoup

html = "<html><body><form><input type='password' name='password' value='secretpassword'></form></body></html>"
soup = BeautifulSoup(html, 'html.parser')
password_value = soup.find('input', {'name': 'password'})['value']
print(password_value)