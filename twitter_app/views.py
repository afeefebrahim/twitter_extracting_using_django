from django.shortcuts import render
from models import Tweets
# Create your views here.
import json
import oauth2 as oauth
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect

def index(request):
    twitter_id = Tweets.objects.order_by('-tweet_id')
    context_dict = {"twitter_id":twitter_id}
    return render(request,'twitter_app/index.html',context_dict)

def new_id(request):
    if request.method == 'POST':
        twit_id = request.POST.get('name')
        print twit_id
        ten_tweets = tweets_extract(twit_id)
        print ten_tweets
        Tweets.objects.create(tweet_id = twit_id,tweets = ten_tweets)
    return render(request,'twitter_app/new_id.html',{}) 
def update(request,pk):
     p = Tweets.objects.get(pk = pk)
     t_id = p.tweet_id
     tweet = tweets_extract(t_id)
     p.tweet_id = t_id
     p.tweets =  tweet
     p.save()
     #HttpResponseRedirect('/twitter_app/')
     return redirect(index) 

def tweets_extract(twitter_id):
    CONSUMER_KEY = "EYWnxAbRGnpu0lVXKh75bBCfA"
    CONSUMER_SECRET = "HygKNaP6wV02i9tcQnQN4C3PJsIlwwLjO9gi78xiDpBqByzXfG"
    ACCESS_KEY = "4922482113-fF3ke1DRtqZMbgNAcgNcs1qJwzxnMcbvUqDA9le"
    ACCESS_SECRET = "GUaVIVUi04fJ8oRnPUKlrqwgFzHCw7pZX6Z3Eem5e4c3i"
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+twitter_id+"&count=10"
    print url
    client = oauth.Client(consumer, token)
    response, content = client.request(url)
    tw = ""
    data = json.loads(content) 
    for i in range(10):
        tw = tw+(data[i]["text"])+"\n"
        #tw.append(data[i]["text"])
    print tw    
    return tw
       
def show(request,pk):
    p = Tweets.objects.get(pk = pk)
    context_dict = {}
    context_dict["twitter_id"] = p.tweet_id
    tw = p.tweets.split('\n')
    context_dict["tweets"] = tw
    print tw
    return render(request,'twitter_app/show.html',context_dict)
