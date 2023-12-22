from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import json

# Creating an instance of webdriver
browser = webdriver.Chrome()

# Goodreads login page
browser.get('https://www.goodreads.com/ap/signin?language=en_US&openid.assoc_handle=amzn_goodreads_web_na&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.goodreads.com%2Fap-handler%2Fsign-in&siteState=07cd4b27f781959df9398944c52827d8')

# Let the user see and also load the element
time.sleep(2)
print("Logging in to Goodreads")

# Find username input
user = browser.find_element(By.XPATH, '//*[@id="ap_email"]')
user.send_keys('your_user_email')

# Find password input
password = browser.find_element(By.XPATH, '//*[@id="ap_password"]')

# Read password from a text file
with open('text.txt', 'r') as myfile:
    Password = myfile.read().replace('\n', '')
password.send_keys(Password)

# Sign in
login_button = browser.find_element(By.XPATH, '//*[@id="signInSubmit"]')
login_button.click()

print("Login Successful")
time.sleep(2)

def get_genre_url(genre_urls):
    genres = ['art', 'biography', 'business', 'children-s', 'christian', 'classics', 'comics', 'cookbooks', 'ebooks', 'fantasy', 'fiction', 'graphic-novels', 'historical-fiction', 'history', 'horror', 'memoir', 'music', 'mystery', 'non-fiction', 'poetry', 'psychology', 'romance', 'science', 'science-fiction', 'self-help', 'sports', 'thriller', 'travel', 'young-adult']
    url_start = 'https://www.goodreads.com/shelf/show/'

    for genre in genres:
        for x in range(1, 10):
            genre_url = f'{url_start}{genre}?page={x}'
            genre_urls.append(genre_url)
    time.sleep(2)

def get_book_url(book_urls, browser, genre_url):
    browser.get(genre_url)

    try:
        # Wait for the element to be present on the page
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="bodycontainer"]/div[3]/div[1]/div[2]/div[3]'))
        )

        body = browser.find_element(By.XPATH, '//*[@id="bodycontainer"]/div[3]/div[1]/div[2]/div[3]')

        # Using find_elements to get a list of elements
        titles = body.find_elements(By.CLASS_NAME, 'bookTitle')

        for title in titles:
            link = title.get_attribute('href')
            book_urls.append(link)

    except NoSuchElementException:
        print(f"Element not found on {genre_url}")

if __name__ == "__main__":
    genre_urls = []
    book_urls = []

    get_genre_url(genre_urls)

    for genre_url in genre_urls:
        get_book_url(book_urls, browser, genre_url)

    # Write data to a JSON file
    with open("book_urls.json", "w", encoding="utf-8") as file:
        json.dump(book_urls, file, indent=4, ensure_ascii=False)

    # Closing the browser
    browser.quit()
