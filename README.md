# Books-Stats-From-Goodreads

This is a personal project to learn more Django, to try out Svelte and of course for the love of books! 

### Analyze your read books data from Goodreads.com, just export out the CSV file containing your books and place in /books folder. More data such as book covers will use the https://openlibrary.org/ API and the prices will be scrapped of amazon.com 

## What you need:
- Python 3
- Django
- Django Rest Framework
- Beautifulsoup4
- Svelte
- Frappe Charts

Make sure to make migrations before starting.

# Backend
Place the CSV-file in **/books** folder
Change name to your filename in  ``` base = str(BASE_DIR) + "/books/booksfile.csv" ``` in the **utils.py** file in **/books/**
When requsting the ``` http://127.0.0.1:8000/ ``` page it will start add the data to the sqlite3 db. 
It will only run if there are no books in the database at the moment so to add new books you have to clean the db and then add the new CSV-file.
After that it will start fetching the prices, Read about it the Price component below.

# Frontend
## The components:
### App.svelte
The start page that loads the other components
### Totalbooks.svelte
Renders the total number of read books, to read books and currently reading books.
### Booksinyears.svelte
Draws a graph of the number of books read in every year. You can configure this to match your data-set better in the **/books/models.py years()** function.
### Categories.svelte
Make a Pie chart of all the book-shelvs you have on goodreads. You can choose which shelves to be included in **/books/models.py category()** function
### Pages.svelte
Calculates a bunch of data about all the pages of the books read.
### Months.svelte
See how many books you read each month every year and compare them. Also see what months in total that most books are read. Change the years to graph in the **months()** function in **/books/models.py**
### Prices.svelte
  Scrappes Amazon for book prices based on the title of the book. For about every 100th book Amazon will stop the scrapping. Then in **/books/utils.py searchBookPrice()**    function just change ``` opener.addheaders = [('User-agent', 'Mozilla/4.8')] ``` to another version and reload and it will keep adding more books. Also since it just uses the title of the book for searching you might get some wrong prices, however this is meant only to give an estimate of the total book price
### Randomtips.svelte
  Gets a random book that has a 5 in user-rating and displays it. The Cover page is loaded from the Openlibrary API if it finds any.
  
## Updates and improvments in the future
 - Host it online
 - Make a better price scrapping function that uses both title, author name to get the prices.
 - Display a “Cover not found” text if the API did´t retrieve any cover.
 - Make it possible to upload a file directly on the page
 - Add users so that others can register and upload their CSV
 - Add other components such as, Calculate reading speed.
 - Make visual comparisons from the data about the height, weight and size
  
  
  
I would be grateful for questions or suggestions. If you know any other similar Goodread data-analyzer please contact me. 


Thanks for reading, 


