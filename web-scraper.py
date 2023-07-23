import requests
from bs4 import BeautifulSoup

def scrape_books():
    base_url = "https://books.toscrape.com"
    page_number = 1
    all_books = []

    while True:
        url = f"{base_url}/catalogue/page-{page_number}.html"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
            
            if not books:
                break
            
            for book in books:
                title = book.h3.a["title"]
                price = book.find("p", class_="price_color").text.strip()
                all_books.append({"title": title, "price": price})
            
            page_number += 1
        else:
            break

    return all_books

if __name__ == "__main__":
    books = scrape_books()
    for book in books:
        print(f"Title: {book['title']}, Price: {book['price']}")
