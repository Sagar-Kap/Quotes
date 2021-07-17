import requests 
from bs4 import BeautifulSoup as soup
import csv

page_num=1
URL = "https://quotes.toscrape.com/page/"+str(page_num)+"/"             

def get_url():
	"""This function performs a GET request to URL
	passed as a parameter within its execution"""                   			 
	with requests.Session() as session:
		return session.get(URL)

def make_soup():
	"""Function returns a soup object stored in the variable""" 
	return soup(get_url().text, "html.parser")
	

def get_container_array():
	"""Function finds out all HTML containers with the quotes 
	and authors' names and returns an array""" 
	text_boxes_array= make_soup().findAll("div", {"class" : "quote"})
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

def fill_csv():
	"""Function compiles the quotes and 
	author's name into a csv file for all web pages, quotes.csv"""
	with open("quotes.csv", "w", newline="") as file:
		thewriter = csv.writer(file)
		thewriter.writerow(["Quote", "Author"])
		serial_num=1
		global page_num

		while page_num<=10:
			for i in get_container_array():
				print(str(serial_num)+". " + get_quote(i) + get_author_name(i))
				thewriter.writerow([get_quote(i), get_author_name(i)])
				serial_num+=1
			page_num+=1
		

fill_csv()