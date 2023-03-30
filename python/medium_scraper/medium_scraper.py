## importing libraries
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def write_page(url, save_name):
    ## creating a request object
    req = Request(url = url,
                  headers = {"User-agent":"Mozilla/5.0"})
    ## getting the page
    try:
        # page = requests.get(url).content
        page = urlopen(req).read()
    except:
        print("Error getting page. Please check your url")
        return
    
    soup = BeautifulSoup(page, "lxml")

    with open(f"scraped_files/{save_name}.html", "w", encoding = "utf-8") as file:
        file.write(soup.prettify())


if(__name__ == "__main__"):
    print("Welcome, ready to scrape some medium?")
    url = input("Page URL >> ")
    save_name = input("Page savename >> ")

    print("Working ..... ")
    write_page(url, save_name)
    print("Done !!")