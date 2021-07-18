import requests 
from bs4 import BeautifulSoup as soup
import csv

page_num=1
URL = "https://quotes.toscrape.com/page/"+str(page_num)+"/"             

def get_url(url):
	"""This function performs a GET request to URL
	passed as a parameter within its execution"""                   			 
	with requests.Session() as session:
		return session.get(url)

def make_soup(url):
	"""Function returns a soup object stored in the variable""" 
	return soup(get_url(url).text, "html.parser")
	

def get_container_array(url):
	"""Function finds out all HTML containers with the quotes 
	and authors' names and returns an array""" 
	text_boxes_array= make_soup(url).findAll("div", {"class" : "quote"})
	return text_boxes_array

def get_quote(a):
	"""Function finds the quote from the 
	selected HTML container passed to it as an argument""" 
	quote= a.find("span", {"class" : "text"})
	return quote.get_text()

def get_author_name(b): 
	"""Function returns the author's name from the HTML container passed to it
	as an argument"""
	author = b.find("small", {"class" : "author"})
	return author.get_text()

def fill_csv(url):
	"""Function compiles the quotes and 
	author's name into a csv file for all web pages, quotes.csv"""
	with open("quotes.csv", "w", newline="") as file:
		thewriter = csv.writer(file)
		thewriter.writerow(["Quote", "Author"])
		serial_num=1

		for container in get_container_array(url):
			print(str(serial_num)+". " + get_quote(container) + get_author_name(container))
			thewriter.writerow([get_quote(container), get_author_name(container)])
			serial_num+=1

def multi_page():
	"""Function will loop through each page
	of site and invoke scraping func fill_csv() on each"""
	Page_Num= 1
	page_url= "https://quotes.toscrape.com/page/"+str(Page_Num)+"/" 

	while Page_Num <= 10:
		fill_csv(page_url)
		Page_Num+=1

multi_page()

