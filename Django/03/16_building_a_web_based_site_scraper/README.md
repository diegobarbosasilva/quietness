python manage.py shell

>>> import requests
>>> page = requests.get('http://www.google.com')
>>> page
<Response [200]>
>>> page.text
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(page.text, 'html.parser')
>>> soup
>>> print(soup.prettify())
>>> soup.find_all('a')
>>> for link in soup.find_all('a'):
....    print(link)
....    -enter-
>>> for link in soup.find_all('a'):
....    print(link.get('href')) 