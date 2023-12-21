import pandas as pd
import re
import string
from datetime import datetime
import nltk
from nltk.corpus import stopwords
from googletrans import Translator

nltk.download('stopwords')

def text_cleaning_lighter(text):
    if (text == ''):
        return text
    try: 
        # replace punctuation with spaces
        translation_table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        text = text.translate(translation_table)
        # to lower case
        # text = text.lower()
        text = re.sub('[^A-Za-z0-9]+', ' ', str(text).lower()).strip()
        # removes special charecters, emojis, texts
        emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                u"\U00002500-\U00002BEF"  # chinese char
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642" 
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"  # dingbats
                                u"\u3030"
                                "]+", flags=re.UNICODE)
        text = emoji_pattern.sub(r'', text)
        # remove multiple spaces
        text = re.sub(' +', ' ', text)
        return text
    except Exception as e:
        print(f"{e}: {text.name}")
        return text

def text_cleaning(text):
    if (text == ''):
        return ''
    try:
        # translate text to English
        translator = Translator()
        text = translator.translate(text, dest='en').text
        # remove meaningless words (stopwords)
        english_stopwords = set(stopwords.words('english'))
        text = [word for word in text.split() if word.lower() not in english_stopwords]    
        text = ' '.join(text)
        # replace punctuation with spaces
        translation_table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        text = text.translate(translation_table)
        # to lower case
        # text = text.lower()
        text = re.sub('[^A-Za-z0-9]+', ' ', str(text).lower()).strip()
        # removes special charecters, emojis, texts
        emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                u"\U00002500-\U00002BEF"  # chinese char
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642" 
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"  # dingbats
                                u"\u3030"
                                "]+", flags=re.UNICODE)
        text = emoji_pattern.sub(r'', text)
        # remove multiple spaces
        text = re.sub(' +', ' ', text)
        return text
    except Exception as e:
        print(f"{e}: {len(text)}")
        return text
    
# text = "Amazon SageMaker Data Wrangler là một tính năng của Amazon SageMaker🤓⚡️, cho            #####@@@ phép bạn chuẩn bị dữ liệu cho ML một cách nhanh chóng và dễ dàng.❤️📚🎧🎬⚠️ Với Amazon SageMaker Data Wrangler, bạn có thể hoàn thành mỗi bước của luồng công việc chuẩn bị dữ liệu, bao gồm lựa chọn, làm sạch, khám phá, phát hiện sai lệch và trực quan hóa dữ liệu từ một giao diện trực quan duy nhất. "
# print(text_cleaning(text))


def convert_to_categorical(genre_str):
    # Evaluate the string to convert it to a list
    genre_list = eval(genre_str)

    # Convert the list to a set to remove duplicate genres
    unique_genres = set(genre_list)

    # Create categorical variables for each genre
    categorical_variables = pd.Categorical(unique_genres)

    return categorical_variables

# Unix timestamp to year
def timestamp_to_year(timestamp):
    try:
        return pd.to_datetime(timestamp, unit='ms').year
    except pd.errors.OutOfBoundsDatetime:
        return pd.NaT


def extract_numeric_rating(rating_string):
    # Split the string and extract the numeric part
    try:
        numeric_rating = int(rating_string.split()[1])
        return numeric_rating
    except (ValueError, IndexError):
        # Handle cases where the extraction fails
        print("Error: Unable to extract numeric rating.")
        return None

# Example usage:
# rating_string = "Rating 4 out of 5"
# numeric_rating = extract_numeric_rating(rating_string)

# if numeric_rating is not None:
#     print(f"The numeric rating is: {numeric_rating}")