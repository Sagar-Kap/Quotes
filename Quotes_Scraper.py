from urllib.request import urlopen as open_url
from bs4 import BeautifulSoup as soup

url = "http://quotes.toscrape.com/"

def scraper():

	def soup_maker():
		request= open_url(url)
		url_reader= request.read()
		page_soup= soup(url_reader, "html.parser")
		request.close()
		return page_soup

	def extract_array_quotes():
		soup_maker(url)
		quotes_array = page_soup.findAll("span", {"class": "text"})
		return quotes_array

	def extract_quotes():
		extract_array_quotes()
		for q in quotes_array:
			quotes= q.get_text()
			print(quotes+"\n\n")


scraper()



