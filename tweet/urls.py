from django.urls import path
from . import views

urlpatterns = [
    path('newtweet/', views.NewTweet),
    path('tweetdetail/<int:tweet_id>/', views.TweetDetail),
    path('authordetail/<int:author_id>/', views.AuthorDetail),
    path('followme/<int:author_id>/', views.FollowMe)
]
