from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium options and the Chrome driver
options = Options()
driver = webdriver.Chrome(options=options)

url= 'https://www.goodreads.com/'
driver.get(url)

# crawl url of genres
genre_urls = []
elements = driver.find_element(By.XPATH, '//*[@id="browseBox"]/div[2]')

links = elements.find_elements(By.TAG_NAME,'a')
prefix = "https://www.goodreads.com/genres/"
url_start = 'https://www.goodreads.com/shelf/show/'

for link in links:
    genre = link.get_attribute('href')
    genre = genre.replace(prefix, "")
    genre_urls.append(genre)

print(genre_urls)