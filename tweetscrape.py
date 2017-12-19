from selenium import webdriver
from time import sleep
import datetime
import sys
from bs4 import BeautifulSoup
import pandas as pd
from textblob import TextBlob
import re


def format_day(date):
    day = '0' + str(date.day) if len(str(date.day)) == 1 else str(date.day)
    month = '0' + str(date.month) if len(str(date.month)) == 1 else str(date.month)
    year = str(date.year)
    return '-'.join([year, month, day])


def form_url(choice, since, until, query, user):
    if(choice=="2"):
        p1 = 'https://twitter.com/search?'
        p2 = 'q=' + query.replace(" ", "%20") + '%20since%3A' + since + '%20until%3A' + until + 'include%3Aretweets&src=typd'
        return p1 + p2
    else:
        p1 = 'https://twitter.com/search?f=tweets&vertical=default&q=from%3A'
        p2 = user + '%20since%3A' + since + '%20until%3A' + until + 'include%3Aretweets&src=typd'
        return p1 + p2


def increment_day(date, i):
    return date + datetime.timedelta(days=i)

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w +:\ / \ / \S +)", " ", tweet).split())

def calc_sentiment(text):
    blob = TextBlob(clean_tweet(text))
    return [blob.sentiment.polarity,len(blob.split(" "))]

def findret(row):
    return (row["Close"] - row["Open"])/row["Open"]

################################################ SETUP PANEL #############################################
choice=input("1. Check using UserID\n2. Check by keyword.")
if(choice=="1"):
    user = input("Enter the user Handle: ")
elif(choice=="2"):
    query=input("Enter the keyword: ")
else:
    print("Invalid Choice. Aborting...")
    sys.exit()

start = datetime.datetime(2012, 11, 5)  # year, month, day
end = datetime.datetime(2017, 11, 3)  # year, month, day

delay = 2
driver = webdriver.Chrome("C:\\Users\\hp pc\\Desktop\\chromedriver.exe")

days = (end - start).days + 1
id_selector = '.time a.tweet-timestamp'
tweet_selector = 'li.js-stream-item'
user = user.lower()
ids = []

ixic = pd.read_csv("C:/Users/hp pc/Downloads/IXIC.CSV", header=0)
gspc = pd.read_csv("C:/Users/hp pc/Downloads/GSPC.CSV", header=0)
dji = pd.read_csv("C:/Users/hp pc/Downloads/DJI.CSV", header=0)

ixic["RET"] = ixic.apply(findret, axis=1)
gspc["RET"] = ixic.apply(findret, axis=1)
dji["RET"] = ixic.apply(findret, axis=1)

final = pd.DataFrame({'Date': list(pd.to_datetime(ixic['Date']).dt.date), 'ixic_ret': list(ixic["RET"]), 'gspc_ret': list(gspc["RET"]), 'dji_ret' : list(dji["RET"])})
final["Polarity"] = 0
final["Word Count"] = 0

d1 = format_day(increment_day(start, 0))
d2 = format_day(increment_day(start, 1))

for day in range(days):
    d1 = format_day(increment_day(start, 0))
    d2 = format_day(increment_day(start, 1))
    url = form_url(choice, d1, d2, query, user)
    print(url)
    print(d1)
    df = datetime.datetime.strptime(d1, '%Y-%m-%d').date()
    driver.get(url)
    sleep(delay)

    found_tweets = driver.find_elements_by_css_selector(tweet_selector)
    increment = 10

    while len(found_tweets) >= increment:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(delay)
        found_tweets = driver.find_elements_by_css_selector(tweet_selector)
        increment += 10

    for tweet in found_tweets:
        id=""
        try:
            id = tweet.find_element_by_class_name("js-tweet-text-container").find_element_by_tag_name("p").text
        except:
            continue
        soup = BeautifulSoup(id)
        text = re.sub(r"http\S+", "",soup.get_text()).lower()
        param = calc_sentiment(text)

        final.loc[final['Date'] == df,'Polarity'] += param[0]
        final.loc[final['Date'] == df, 'Word Count'] += param[1]
    if choice == 1:
        final.to_csv("C:/Users/hp pc/Downloads/final(user)_" + user + ".CSV", index=False)
    else:
        final.to_csv("C:/Users/hp pc/Downloads/final(query)_" + query + ".CSV", index=False)

    start = increment_day(start, 1)
print('all done here')
driver.close()