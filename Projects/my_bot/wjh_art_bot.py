import tweepy
import time


#1369900332407394306-60an2fTakLqVdgcS9SI0g4QPSdSeGh ACCESS TOKEN
#1bivGx1ZNDNa6VhoteAi4tJlRYcfc8mzDt6MjPnxRHAkf ACCESS TOKEN SECRET
#BXpdmst5VnieUpzShW1QbWn7u API KEY
#5ULmig3keJc6DODSG1PxMlLdzTDgvKeC9fWyNJqsuM1NEe9CCr API KEY SECRET
#AAAAAAAAAAAAAAAAAAAAAG%2BFTwEAAAAANW5SY2IhnCOWQYOUIqsh1Dv3%2B5A%3DddZ9Msh5pqJlS1RR32hw2eTA0hBFjVO24fhX5pSq3oDlI9UJmJ BEARER TOKEN

print("this is my twitter bot", flush=True)

CONSUMER_KEY = "BXpdmst5VnieUpzShW1QbWn7u"
CONSUMER_SECRET = "5ULmig3keJc6DODSG1PxMlLdzTDgvKeC9fWyNJqsuM1NEe9CCr"
ACCESS_KEY = "1369900332407394306-60an2fTakLqVdgcS9SI0g4QPSdSeGh"
ACCESS_SECRET = "1bivGx1ZNDNa6VhoteAi4tJlRYcfc8mzDt6MjPnxRHAkf"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = "last_seen_id.txt"

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, "r")
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print("retrieving and replying to tweets...", flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode="extended")
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if "#helloworld" in mention.full_text.lower():
            print("found #helloworld!", flush=True)
            print("responding back...", flush=True)
            api.update_status('@' + mention.user.screen_name + "#HelloWorld back to you!", mention.id)
while True:
    reply_to_tweets()
    time.sleep(15)
