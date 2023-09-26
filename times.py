import requests
from bs4 import BeautifulSoup

def timesofindia():
    url = "https://timesofindia.indiatimes.com/home/headlines"
    page_request = requests.get(url)
    data = page_request.content
    soup = BeautifulSoup(data, "html.parser")

    counter = 0
    with open("news_articles.txt", "w", encoding="utf-8") as file:
        for divtag in soup.find_all("div", {"class": "headlines-list"}):
            for ultag in divtag.find_all("ul", {"class": "clearfix"}):
                for litag in ultag.find_all("li"):
                    counter = counter + 1
                    article_url = "https://timesofindia.indiatimes.com" + litag.find("a")["href"]

                    try:
                        # Fetch the article page
                        article_request = requests.get(article_url)
                        article_data = article_request.content
                        article_soup = BeautifulSoup(article_data, "html.parser")

                        # Extract title and date
                        article_title_tag = article_soup.find("h1")
                        article_byline_div = article_soup.find("div", {"class": "xf8Pm byline"})

                        # Check if the tags exist before extracting content
                        if article_title_tag:
                            article_title = article_title_tag.text.strip()
                        else:
                            article_title = "Title not found"

                        if article_byline_div:
                            article_date_tag = article_byline_div.find("span")
                            if article_date_tag:
                                article_date = article_date_tag.text.strip()
                            else:
                                article_date = "Date not found"
                        else:
                            article_date = "Date not found"

                        # Extract content stored in div with class "_s30J clearfix"
                        article_content_div = article_soup.find("div", {"class": "_s30J clearfix"})
                        if article_content_div:
                            article_content = article_content_div.text.strip()
                        else:
                            article_content = "Content not found"

                        # Write title, content, and date to the text file
                        file.write(f"Article {counter}:\n")
                        file.write(f"Title: {article_title}\n")
                        file.write(f"Content: {article_content}\n")
                        file.write(f"Date: {article_date}\n\n")
                        print(f"Article {counter} saved to news_articles.txt")

                    except Exception as e:
                        print(f"Error processing article {counter}: {str(e)}")

if __name__ == "__main__":
    timesofindia()
