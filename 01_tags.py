import requests
from bs4 import BeautifulSoup

with open("web scrapper/sample.html","r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,"html.parser")
# print(soup.prettify())
# print(soup.find_all('a'))
tag = soup.p
print(type(tag))
