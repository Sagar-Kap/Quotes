import requests
from bs4 import BeautifulSoup as soup

url = "http://quotes.toscrape.com/"

def get_soup(url):

	page = request.get(url)
	page_soup= soup(page, "html.parser")
	return(page_soup)

get_soup(url)

