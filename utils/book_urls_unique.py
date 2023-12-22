import json

# read data
with open('book_urls.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# clear duplicated data
unique_data = list(set(data))

# write to new file
with open('book_urls_unique.json', 'w', encoding='utf-8') as file:
    json.dump(unique_data, file, indent=4, ensure_ascii=False)
