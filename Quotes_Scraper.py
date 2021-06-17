import requests
from bs4 import BeautifulSoup as soup

url = "http://quotes.toscrape.com/"

def get_soup(url):

	page = requests.get(url)

	page_soup= soup(page.text, "html.parser")
	print(page_soup)

get_soup(url)

