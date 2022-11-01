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
def searchBookPrice(searchCode):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(f'https://www.amazon.se/s?k={searchCode}')
    html_contents = response.read()       
    soup = BeautifulSoup(html_contents, 'html.parser')

    Check = soup.find_all('span', class_='a-size-base a-color-base')
    print("CHECK", Check)

    if Check:
        price = soup.find_all('span', class_='a-price-whole')    
        #price = re.sub('[^0-9]', '', price)
        #price = int(price)        
        print("price", price)
        return price
    else:
        return 0

def priceUpdates():
    hits = 0
    misses = 0

    books = Books.objects.all()[5:6]
    print("book",books)

    for book in books:
        if book.ISBN13 > 0:
           print("IN ISBN13: ", book.ISBN13)
           price = searchBookPrice(book.ISBN13)
           print("ISBN13", book.title[:40], "PRICE", price, book.ISBN13)
        """
        title = re.sub('[^A-Za-z0-9]+', '', book.title)
        print("IN ISBN", title)
        price = searchBookPrice(title)
        print("TITLE", book.title, "PRICE", price)        
        if book.ISBN13 > 0:
            print("IN ISBN13")
            price = searchBookPrice(book.ISBN13) 
            print("ISBN13", book.title[:40], "PRICE", price, book.ISBN13)       
        elif len(book.ISBN) == 10 :
            print("IN ISBN")
            price = searchBookPrice(book.ISBN)
            print("ISBN", book.title[:40], "PRICE", price)
        else:
        """          

    




