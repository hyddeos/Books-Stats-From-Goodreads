import pandas
from bookproject.settings import BASE_DIR
from books.models import Books
import datetime
from bs4 import BeautifulSoup
import urllib.request as urllib2
import re


def Run():

    print("Reading CSV")
    base = str(BASE_DIR) + "/books/booksfile.csv"
    file = pandas.read_csv(base)


    # Remove =""// etc
    file['ISBN'] = file['ISBN'].str.replace('\W', '0', regex=True)
    file['ISBN13'] = file['ISBN13'].str.replace('\W', '0', regex=True)
    file['Date Read'] = file['Date Read'].str.replace('\W', '-', regex=True)
    file['Date Added'] = file['Date Added'].str.replace('\W', '-', regex=True)
    file['Year Published'] = file['Year Published'].astype(str).apply(lambda x: x.replace('.0',''))
    file['Original Publication Year'] = file['Original Publication Year'].astype(str).apply(lambda x: x.replace('.0',''))
    
    # Remove Nan, set to 0    
    file['Book Id'] = file['Book Id'].fillna(0)
    file['ISBN13'] = file['ISBN13'].fillna(0)
    file['My Rating'] = file['My Rating'].fillna(0)
    file['Average Rating'] = file['Average Rating'].fillna(0)
    file['Number of Pages'] = file['Number of Pages'].fillna(0)
    file['Read Count'] = file['Read Count'].fillna(0)
    file['Year Published'] = file['Year Published'].fillna(0)
    file['Original Publication Year'] = file['Original Publication Year'].fillna(0)
    file['Date Read'] = file['Date Read'].fillna(0)
    file['Date Added'] = file['Date Added'].fillna(0)
    
    file_array = file.to_dict(orient="records")
    
    print("Len", len(file_array))
    for entry in file_array:
        try:            
            if not entry['Date Read']:
                entry['Date Read'] = "1000-01-01"            

            book = Books(            
                goodreadsID = entry["Book Id"],
                title = entry["Title"],
                authorLF = entry["Author"],
                authorFL = entry["Author l-f"],
                ISBN = entry["ISBN"],
                ISBN13 = entry["ISBN13"],
                myRating = entry["My Rating"],
                avgRating = entry["Average Rating"],
                publisher = entry["Publisher"],
                pages = entry["Number of Pages"],
                published = entry["Year Published"],
                firstpublished = entry["Original Publication Year"],
                dateRead = entry["Date Read"],
                dateAdded = entry["Date Added"],
                bookShelves = entry["Bookshelves"],
                readStatus = entry["Exclusive Shelf"],
                readCount = entry["Read Count"],
            )
            book.save()
        except SyntaxError:
            print("SyntaxError")
            pass
    print("Save done")
    return


# Updates the prices
def searchBookPrice(book):
    title = re.sub(r"[^a-zA-Z0-9 ]", "", book.title)
    titleSearch = title.replace(" ", "+")    
    opener = urllib2.build_opener()
    # If many books Amazon will block and program will stop, Then just change Version and go again
    opener.addheaders = [('User-agent', 'Mozilla/4.8')] 
    response = opener.open(f'https://www.amazon.se/s?k={titleSearch}')
    html_contents = response.read()       
    soup = BeautifulSoup(html_contents, 'html.parser')

    check = soup.find_all('span', class_='a-color-state a-text-bold')

    if check:
        try:
            price = soup.find_all('span', class_='a-price-whole')
            price = price[0].get_text()
            price = price.replace(",", "")
            print("Price", price, "Title:", book.title)
            price = float(price)            
            if price > 0:
                book.price = price
                book.save()
                return 1
            else:
                return 0
        except:
            return 0

def priceUpdates():
    priceFound = 0
    priceNotFound = 0

    books = Books.objects.all()

    for book in books:
        if book.price == 0:
            tempBook = searchBookPrice(book)
            if tempBook == True and tempBook > 0:
                priceFound += 1
            else:
                priceNotFound +=1
    return None




    




