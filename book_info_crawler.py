import requests
from time import time
import json
from bs4 import BeautifulSoup
import ftfy

data_items = []
prefix = "https://www.goodreads.com/user/show/"

def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("h1", class_="Text Text__title1")
    rate = soup.find('div', class_="RatingStatistics__column")
    author = soup.find('span', class_='ContributorLink__name')
    published_date = soup.find('p', {'data-testid': 'publicationInfo'})
    if published_date:
        published_date = published_date.get_text(strip=True).split(', ')[1]
    else:
        published_date = None
    
    page_numbers = soup.find('p', {'data-testid': 'pagesFormat'})
    if page_numbers:
        page_numbers = page_numbers.get_text(strip=True).split(' ')[0]
    else:
        page_numbers = None
    price = soup.select_one('button.Button--buy span.Button__labelItem')
    if price:
        price = price.get_text(strip=True)
        if '$' in price:
            price = price.split('$')[1]
        else:
            price = None
    else:
        price = None

    description = soup.find('span', class_='Formatted')
    genre_ul = soup.find('ul', class_='CollapsableList')
    genre_list = genre_ul.find_all('span', class_='Button__labelItem')
    reviews = soup.find('div', class_='ReviewsSection')
    articles = reviews.find_all('article', class_='ReviewCard')
    
    max_iterations = 31
    iteration_count = 0

    for article in articles:
        if iteration_count >= max_iterations:
            break

        user_link = article.find('a', class_='Avatar Avatar--medium')
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
            "title": title.get_text(strip=True) if title else None,
            "rate": rate.get_text(strip=True) if rate else None,
            "author": author.get_text(strip=True) if author else None,
            "published": published_date,
            "page_numbers": page_numbers,
            "price": price,
            "description": description.get_text(strip=True) if description else None,
            "genre": genre_list[0].get_text(strip=True) if genre_list else None,
            "user": user,
            "user_rate": user_rate,
            "user_review": user_review,
        }
        data_items.append(item)
        iteration_count += 1
        print(iteration_count)

def read_strings_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        if isinstance(data, list):
            return data
        else:
            return None

def crawl_list():
    url_list = read_strings_from_json("./book_urls_unique.json")
    # thay đổi số lượng ở url_list[số bắt đầu:số kết thúc]
    for url in url_list[20:40]:
        get_data(url)       

if __name__ == "__main__":
    crawl_list()
    with open("final_data.json", "w", encoding='utf-8') as file:
        json.dump(data_items, file, indent=4, ensure_ascii=False)
