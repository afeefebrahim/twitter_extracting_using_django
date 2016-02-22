from django.db import models

# Create your models here.
class Tweets(models.Model):
	tweet_id = models.CharField(max_length = 30,null = True)
	tweets = models.CharField(max_length = 500)
	def __str__(self):
		return self.tweet_id