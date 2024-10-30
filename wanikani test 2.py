from wanikani_api.client import Client
import pandas as pd
import os

df = pd.DataFrame()

v2_api_key = os.getenv("WANIKANI_API") # You can get it here: https://www.wanikani.com/settings/account
client = Client(v2_api_key)
user_information = client.user_information()
words = []
mean = []
all_vocabulary = client.subjects(types="vocabulary", fetch_all=True)
for word in all_vocabulary:
    words.append(word.characters)
for meaning in all_vocabulary:
    mean.append(meaning.meanings[0].meaning)
print(words)
print(len(words))
print(mean)
print(len(mean))
df["Vocab"] = words
df["Meaning"] = mean
df.to_csv("vocab.csv", index=False)
# token =