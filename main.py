

from tkinter.messagebox import RETRY
import urllib.parse
import requests
from bs4 import BeautifulSoup
import logging
from requests.exceptions import RequestException
import urllib


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_and_print_a_tags(raw_url,num_of_results):
    url = ""
    logging.info(f"Fetching URL: {url}\n\n")
    for i in range(0,num_of_results,10):
        try:
            url = raw_url+f"&start={i}"
            # Send a GET request to the webpage
            response = requests.get(url, timeout=10)

            # Check if the request was successful
            response.raise_for_status()

            # Parse the content of the webpage with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            titles = soup.find_all("h3")
            for title in titles:
                url_element = title.parent.parent.parent
                url = url_element["href"].replace("/url?q=","")
                
                print(f"Title: {title.text}")
                print(f"Url: {url}\n")
                


        except RequestException as e:
            logging.error(f"Error fetching the URL: {url} - {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

def get_encoded_url(query):
    base_url = 'https://www.google.com/search?q='
    encoded_query = urllib.parse.quote(query)
    return base_url+encoded_query

if __name__ == "__main__":
    # URL of the webpage to scrape
    query = input("Enter Your Query: ")
    num_of_results = int(input("Enter Number Of results You want."))
    url = get_encoded_url(query)
    fetch_and_print_a_tags(url,num_of_results)

