import pandas as pd
import re
import string


def convert_to_categorical(df, column):
    
    # Check if the specified column exists in the dataframe
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in the dataframe.")

    # Convert the specified column to categorical
    df[column] = df[column].astype('category')

    return df


def text_cleaning(text):
    '''
    Converts all text to lower case, Removes special charecters, emojis and multiple spaces
    text - Sentence that needs to be cleaned
    '''
    text = ''.join([k for k in text if k not in string.punctuation])
    text = re.sub('[^A-Za-z0-9]+', ' ', str(text).lower()).strip()
    text = re.sub(' +', ' ', text)
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    return text

# text = "Welcome to my re-read of the timeless series \"Harry Potter\". 🤓⚡️If you've followed along, then you already know, that I'm reading the books, listening to a fun (adult) podcast and watching the movies. ❤️📚🎧🎬⚠️This review contains spoilers⚠️If you don't yet know:*why we wonder if the Dementors blew a new personality into Dudley*why we're calling Harry Barney or Barry, the cousin*the loss of laughter with a twin*why the word \"always\" means more than you know——-Then proceed with extreme caution!——-Spoiler Credit: Podcast: Binge Mode (listen on Spotify)Personal Opinion Note: I'm incredibly sad for you, if you've never read the books (or at least watched the movies). 😉📚🎧🎬 This magical story is worth the time, I promise.We're near the end of this adventure… and…. This book is incredibly sad. So, I'll be updating this review with what I consider to be the most memorable/heartache/important part of each chapter/podcast as I finish.📚Chapter 1: The Dark Lord AscendingThe doubts clearly displayed by the Malfoy's, in choosing the wrong side.📚Chapter 2: In MemoriamRita Skeeter pops her head out of her jar again… and she sucks!📚Chapter 3: The Dursley's DepartingDudley asking why Harry wasn't going with them and his genuine (and uncharacteristic) concern.🎧Podcast: Binge Mode: Chapters 1-3***Warning: Binge Mode contains adult content***Insight into what Petunia was going to say, but just couldn't and the change in Dudley.📚Chapter 4: The Seven PottersRIP Hedwig…. My heart aches.📚Chapter 5: Fallen WarriorRIP Madeye and George's ear (although he is now truly holy).📚Chapter 6: The Ghoul in PajamasRon/Hermione vibes… plus, their insistence on helping Harry.🎧Podcast: Binge Mode: Chapters 4-6***Warning: Binge Mode contains adult content***Further insight into Horcruxe's and splitting of soul.📚Chapter 7: The Will of Albus DumbledoreRufus Scrimgeour proves, yet again, that to be the Minister of Magic, means being an utter twat.📚Chapter 8: The WeddingAunt Muriel really sucks.🎧Podcast: Binge Mode: Chapters 7-8***Warning: Binge Mode contains adult content***The history of the sword of Gryffindor.📚Chapter 9: A Place to HideHermione really is brilliant with her Mary Poppins bag.📚Chapter 10: Kreacher's TaleVoldemort's underestimation and/or complete lack of thought about house elves.📚Chapter 11: The BribeHarry turns Lupin away, in hopes that he'll go back to Tonks.🎧Podcast: Binge Mode: Chapters 9-11***Warning: Binge Mode contains adult content***House elves and Lupin/Harry throw down.📚Chapter 12: Magic is MightRon's trying to protect Hermione and Hermione's trying to protect Ron.📚Chapter 13: The Muggle-born Registration CommissionHarry's impromptu decision to get all the muggle born (awaiting unfair trial) out of the ministry.📚Chapter 14: The ThiefRon getting hurt and the trio hunkering down while he recovers.🎧Podcast: Binge Mode: Chapters 12-14***Warning: Binge Mode contains adult content***All the insights into medical magical things.📚Chapter 15: The Goblin's RevengeHarry and Ron's intense fight and Hermione's forced to choose a side.📚Chapter 16: Godric's HollowThe sadness Harry feels at discovering that the Dumbledore's grave is near his parents.📚Chapter 17: Bathilda's SecretThe snake and the broken wand.🎧Podcast: Binge Mode: Chapters 15-17***Warning: Binge Mode contains adult content***The Potter's family history.📚Chapter 18: The Life and Lies of Albus DumbledoreHermione defending Dumbledore's young past.📚Chapter 19: The Silver DoeRon's timely return.🎧Podcast: Binge Mode: Chapters 18-19***Warning: Binge Mode contains adult content***Exploring Dumbledore's past and how his change helped the trio.📚Chapter 20: Xenophilius LovegoodRon and Hermione's outvoting Harry.📚Chapter 21: The Tale of the Three BrothersThe story of the hollows.📚Chapter 22: The Deathly HollowsLee Jordan, Lupin and Fred being on the radio.🎧Podcast: Binge Mode: Chapters 20-22***Warning: Binge Mode contains adult content***Harry's family ties to the hollows.📚Chapter 23: Malfoy ManorDobby… sweet and loyal to the end…. RIP Dobby.📚Chapter 24: The WandmakerHarry buried Dobby without use of Magic.📚Chapter 25: Shell CottageLupin and Harry's mended relationship.🎧Podcast: Binge Mode: Chapters 23-25***Warning: Binge Mode contains adult content***Interesting insights into apparition long distance.🎬Movie #7: Part 1Considering how much they had to jam pack into this movie, they did a decent job on this one.🎧Podcast: Binge Mode: Movie: Part 1***Warning: Binge Mode contains adult content***The actors really know these characters well at this point.📚Chapter 26: GringottsHermione as Bellatrix feeling ewwwwww.📚Chapter 27: The Final Hiding PlaceHarry's \"Voldemort Vision\" finally coming in handy.📚Chapter 28: The Missing MirrorThe greater good and the Dumbledore's.🎧Podcast: Binge Mode: Chapters 26-28***Warning: Binge Mode contains adult content***Sad. Close to the end.📚Chapter 29: The Lost DiademThe DA members showing up at Hogwarts.📚Chapter 30: The Sacking of Severus SnapeMcGonagall's taking over and standing as leader of Hogwarts.📚Chapter 31: The Battle of HogwartsThe Weasley's really are the best wizard family and my heart aches. 💔🎧Podcast: Binge Mode: Chapters 29-31***Warning: Binge Mode contains adult content***Neville comes full circle and the Ron/Hermione connection.📚Chapter 32: The Elder WandVoldemort finishes Snape and the battle is taking endless lives.📚Chapter 33: The Prince's TaleAll of Snape's secrets. Always. 😭🎧Podcast: Binge Mode: Chapters 32-33***Warning: Binge Mode contains adult content***All the cries and Snape's true self.📚Chapter 34: The Forest AgainAll the losses and Harry's bravery.📚Chapter 35: King's CrossDumbledore's testimony to Harry and his insistence that it's better to live with love.🎧Podcast: Binge Mode: Chapters 34-35***Warning: Binge Mode contains adult content***The fact that JK had chapter 34 down from the beginning.📚Chapter 36: The Flaw in the PlanThe great defeat and celebration.📚Epilogue:The little family. Life continues.🎧Podcast: Binge Mode: Chapters 36-Epilogue***Warning: Binge Mode contains adult content***The sadness that is the end.🎬Movie #7: Part 2This was the best movie adaptation, in my opinion, of the series. I cry buckets when Harry dives into Snape's memories.🎧Podcast: Binge Mode: Movie: Part 2***Warning: Binge Mode contains adult content***All the additions and deductions reviewed but consensus is still- a great movie.This concludes my re-reading of the timelessly magical series. I'm so glad that I took the time to re-read it, but also, that I was able to enjoy Binge Mode Harry Potter on Spotify as well. My heart is full. Thanks for sticking with me on my journey. ❤️📚"
# print(text_cleaning(text))


from datetime import datetime

def timestamp_to_year(timestamp):
    # Convert timestamp to datetime object
    dt_object = datetime.utcfromtimestamp(timestamp)

    # Extract the year from the datetime object
    year = dt_object.year

    return year

# Example usage:
# timestamp = 1083394800000 / 1000  # Replace this with your Unix timestamp
# year_result = timestamp_to_year(timestamp)
# print(f"{timestamp} timestamp corresponds to the year {year_result}.")


def extract_numeric_rating(rating_string):
    # Split the string and extract the numeric part
    try:
        numeric_rating = float(rating_string.split()[1])
        return numeric_rating
    except (ValueError, IndexError):
        # Handle cases where the extraction fails
        print("Error: Unable to extract numeric rating.")
        return None

# Example usage:
rating_string = "Rating 4 out of 5"
numeric_rating = extract_numeric_rating(rating_string)

if numeric_rating is not None:
    print(f"The numeric rating is: {numeric_rating}")