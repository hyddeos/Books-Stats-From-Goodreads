import pandas
from bookproject.settings import BASE_DIR
from books.models import Books

def Run():

    print("Reading csv")
    base = str(BASE_DIR) + "/books/test.csv"
    print("Base", base)
    file = pandas.read_csv(base)

    file_array = file.to_dict(orient="records")
    print("Len", len(file_array))
    for entry in file_array:
        try:
            print(entry["Title"])
            print("test!!")
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