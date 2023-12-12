import pandas as pd
import json

books = pd.read_json('./data/book_test.jl', lines=True)
print(books.head(3))


# Drop columns
print(books.columns)
books.drop(['titleComplete', 'imageUrl', 'asin', 'isbn', 'isbn13', 'publisher', 'series', 'characters', 'places', 'awards'], axis=1, inplace = True)
print(books.columns)