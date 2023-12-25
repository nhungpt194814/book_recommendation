import requests
from time import time
import json
from bs4 import BeautifulSoup
import ftfy

data_items = []
prefix = "https://www.goodreads.com/user/show/"
current_index = 0

def get_data(url):
    global current_index

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    reviews = soup.find('div', class_='ReviewsSection')
    if reviews is None:
        print(f"Skipping URL index {current_index} because of missing 'ReviewsSection'.")
        return

    title = soup.find("h1", class_="Text Text__title1")
    articles = reviews.find_all('article', class_='ReviewCard')
    
    if articles is None:
        print(f"Skipping URL index {current_index} because of missing 'ReviewCard'.")
        return

    max_iterations = 31
    iteration_count = 0

    for article in articles:
        if iteration_count >= max_iterations:
            break
        
        user_link = article.select_one('a.Avatar.Avatar--medium')
        if user_link:
            user = user_link['href'].replace(prefix, "")
        else:
            user = None
        
        user_rate = article.find('span', class_='RatingStars RatingStars__small')
        user_rate = user_rate['aria-label'] if user_rate else None

        user_review_tag = article.find('span', class_='Formatted')
        user_review_1 = user_review_tag.get_text(strip=True) if user_review_tag else None
        user_review = ftfy.fix_text(user_review_1)

        item = {
            "book_url": url,
            "title": title.get_text(strip=True) if title else None,
            "user": user,
            "user_rate": user_rate,
            "user_review": user_review,
        }
        data_items.append(item)
        iteration_count += 1

def read_strings_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        if isinstance(data, list):
            return data
        else:
            return None

def crawl_list():
    global current_index
    url_list = read_strings_from_json("./bookUrlExt.json")

    for url in url_list:
        get_data(url)
        current_index += 1  

if __name__ == "__main__":
    crawl_list()
    with open("bookComment.json", "w", encoding='utf-8') as file:
        json.dump(data_items, file, indent=4, ensure_ascii=False)