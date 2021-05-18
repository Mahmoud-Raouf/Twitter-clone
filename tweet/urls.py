from django.urls import path
from .views import Create_Tweet ,TweetList , HomeView ,UpdateTweet ,DeleteTweet
from . import views
app_name = 'tweet'




urlpatterns = [

    path('' , HomeView.as_view(), name='HomeView'),
    path('<slug:slug>/delete/' , DeleteTweet.as_view(), name='deletetweet'),
    path('<slug:slug>/update/' , UpdateTweet.as_view(), name='updatetweet'),
    # path('add/tweet/', Create_Tweet.as_view(), name='Create_Tweet'),
    # path('', views.tweet_home, name='tweet_home'),
    # path('<int:id>/', views.tweet_detail, name='tweet_detail'),
]