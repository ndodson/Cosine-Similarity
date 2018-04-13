#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "997445084-OtA9zNs9OK5xGsxinCwSK4nCoCK2i4aNPU9J2vB5"
access_token_secret = "LTiHZeOH6jjeQWgJyQ27pOSqJbkCLRC0ax4ZDRo8QdgH9"
consumer_key = "BKjouv31QXtaGFaAWUJYDG8za"
consumer_secret = "WxpQqYD3QpMGmQIfE9ArzDBQzD4ODQ276p35Gp8ah4HARuxRBk"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
