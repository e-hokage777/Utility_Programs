## importing libraries
import requests
from bs4 import BeautifulSoup
import os

# https://towardsdatascience.com/generalised-additive-models-6dfbedf1350a

def write_page(url, save_name):
    ## getting the page
    try:
        page = requests.get(url).content       
    except:
        print("Error getting page. Please check your url")
        return
    
    soup = BeautifulSoup(page, "lxml")

    with open(f"scraped_files/{save_name}.html", "w", encoding = "utf-8") as file:
        file.write(soup.prettify())

def check_n_create_dir():
    print("Checking if 'scraped_files' folder already exists...")
    if not os.path.isdir("./scraped_files"):
        print("Folder does not exist")
        print("Creating folder .... ")

        os.mkdir("./scraped_files")
    else:
        print("'scraped_files folder already exists'")


if(__name__ == "__main__"):
    print("Welcome, ready to scrape some medium?")
    url = input("Page URL >> ")
    save_name = input("Page savename >> ")

    check_n_create_dir()

    print("Working on page ..... ")
    write_page(url, save_name)
    print("Done !!")