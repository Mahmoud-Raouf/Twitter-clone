from django.test import TestCase
from tweet.models import Tweet

class TweetTestCase(TestCase):
    def setUp(self):
        Tweet.objects.create(content="lion")
        Tweet.objects.create(content="cat")

    def test_tweets_can_speak(self):
        lion = Tweet.objects.get(content="lion")
        cat = Tweet.objects.get(content="cat")
