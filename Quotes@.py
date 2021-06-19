import requests
from bs4 import BeautifulSoup as soup

url = "http://quotes.toscrape.com/"

def get_soup(url):

	page = requests.get(url)
	page_soup= soup(page.text, "html.parser")
	return(page_soup)

def get_text(url):

	get_soup(url)
	text_array= page_soup.findAll("div", {"class":"quote"})
	for container in text_array:
		text_container = container.find("span", {"class":"text"})
		text = text_container.get_text()
		print(text+"\n")


get_text(url)
