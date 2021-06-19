import requests
from bs4 import BeautifulSoup as soup

url = "http://quotes.toscrape.com/"

def get_soup(url):

	page = requests.get(url)
	page_soup= soup(page.text, "html.parser")
	return(page_soup)

a= get_soup(url)

def get_text():

	text_array= a.findAll("div", {"class":"quote"})
	for container in text_array:
		text_container = container.find("span", {"class":"text"})
		text = text_container.get_text()
		print(text+"\n")


get_text()
