import requests 
from bs4 import BeautifulSoup as soup

filename= "quotes.csv"
f= open(filename, "w")
headers = "Quotes,Author\n"
f.write(headers)

URL = "http://quotes.toscrape.com/"

def connection(): #form a connection
	with requests.Session() as session:
		return session.get(URL)

def soupa():  #form a soup of the page
	return soup(connection().text, "html.parser")
	

def text_boxes(): #find out the text boxes in the page
	text_boxes= soupa().findAll("div", {"class": "quote"})
	return text_boxes

def quotes(a): #return quotes from the selected div
	quotes= a.find("span", {"class" : "text"})
	return quotes.get_text()

def author(b): #return the author from the selected div
	author = b.find("small", {"class" : "author"})
	return author.get_text()

def text():
	q=1
	for i in text_boxes():
		print(str(q)+". " + quotes(i) + author(i))
		f.write(quotes(i)+","+author(i)+"\n")
		q+=1

text()
f.close()	