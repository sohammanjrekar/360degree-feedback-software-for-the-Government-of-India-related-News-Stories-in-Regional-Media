import os
import requests
from bs4 import BeautifulSoup

# Define a list of website URLs to scrape
website_urls = [
    "https://example2.com/news",
    # Add more website URLs here
]

# Create a directory to save the scraped articles
output_dir = "scraped_articles"
os.makedirs(output_dir, exist_ok=True)

# Function to scrape headlines from a website URL
def scrape_website(url):
    try:
        # Send an HTTP GET request to the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find and extract article headlines
            headlines = soup.find_all('h2', class_='headline-class')  # Adjust based on website structure

            # Process and save the extracted headlines to text files
            for index, headline in enumerate(headlines, start=1):
                title = headline.text.strip()
                filename = os.path.join(output_dir, f"article_{index}.txt")
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(f"Title: {title}\n")

            print(f"Scraping complete for {url}.")
        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")

# Iterate through the list of website URLs and scrape each one
for url in website_urls:
    scrape_website(url)
