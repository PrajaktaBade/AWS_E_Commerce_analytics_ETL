import requests
from bs4 import BeautifulSoup
import sqlite3

url = "http://books.toscrape.com/"
response = requests.get(url)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all book titles and prices
    books = soup.find_all('article', class_='product_pod')
    print(f"Found {len(books)} books on the page.")
    
    book_data = []

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        print(f"Title: {title}, Price: {price}")
        book_data.append((title, price))
    
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    print("Please check the URL or your internet connection.")
    print("Exiting the script.")
    exit(1) 

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price TEXT
)
""")
