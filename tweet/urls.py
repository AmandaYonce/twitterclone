from django.urls import path
from .views import NewTweet, TweetDetail, AuthorDetail, FollowMe, UnfollowMe

urlpatterns = [
    path('newtweet/', NewTweet.as_view()),
    path('tweetdetail/<int:tweet_id>/', TweetDetail.as_view()),
    path('authordetail/<int:author_id>/', AuthorDetail.as_view()),
    path('followme/<int:author_id>/', FollowMe.as_view()),
    path('unfollowme/<int:author_id>/', UnfollowMe)
]
