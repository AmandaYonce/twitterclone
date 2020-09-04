from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import CustomUser
from notification.models import Notification
import re


def NewTweet(request):
    if request.method == "POST":
        form = CreateTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            author_inst = CustomUser.objects.filter(username=request.user.username).first()
            new_Tweet = Tweet.objects.create(
                author=author_inst,
                tweet=data.get('tweet'),
            )
            if data.get('tweet').find('@'):
                pattern = re.compile(r'@')
                contents = data.get('tweet')
                matches = pattern.finditer(contents)
                for match in matches:
                    index=match.span()
                    atter = contents[index[1]::]
                    atter_instance = CustomUser.objects.filter(username=atter).first()
                    Notification.objects.create(
                        at_person=atter_instance,
                        the_tweet=new_Tweet
                    )
            return HttpResponseRedirect(reverse('home'))
    form = CreateTweetForm()
    return render(request, "newtweet.html", {'form': form})


def TweetDetail(request, tweet_id):
    tweet = Tweet.objects.filter(id=tweet_id).first()
    return render(request, 'tweetdetail.html', {"tweet": tweet})


def AuthorDetail(request, author_id):
    author = CustomUser.objects.filter(id=author_id).first()
    count = Tweet.objects.filter(author=request.user).count
    return render(request, 'authordetail.html', {"author": author, 'count': count})


def FollowMe(request, author_id):
    usertofollow = CustomUser.objects.filter(id=author_id).first()
    usertofollow.following.add(request.user.id)
    return HttpResponseRedirect(reverse('home'))


def UnfollowMe(request, author_id):
    usertofollow = CustomUser.objects.filter(id=author_id).first()
    usertofollow.following.remove(request.user.id)
    return HttpResponseRedirect(reverse('home'))
