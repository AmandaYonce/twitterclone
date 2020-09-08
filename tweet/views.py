from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import CustomUser
from notification.models import Notification
import re
from django.views.generic import View


class NewTweet(View):
    template_name = 'newtweet.html'
    form_class = CreateTweetForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
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
        return render(request, self.template_name, {'form': form})


class TweetDetail(View):
    template_name = 'tweetdetail.html'

    def get(self, request, tweet_id):
        tweet = Tweet.objects.filter(id=tweet_id).first()
        return render(request, self.template_name, {"tweet": tweet})


class AuthorDetail(View):
    template_name = 'authordetail.html'

    def get(self, request, author_id):
        author = CustomUser.objects.filter(id=author_id).first()
        count = Tweet.objects.filter(author=author_id).count
        return render(request, self.template_name, {"author": author, 'count': count})


class FollowMe(View):
    template_name = 'home'

    def get(self, request, author_id):
        usertofollow = CustomUser.objects.filter(id=author_id).first()
        usertofollow.following.add(request.user.id)
        return HttpResponseRedirect(reverse(self.template_name))


def UnfollowMe(request, author_id):
    usertofollow = CustomUser.objects.filter(id=author_id).first()
    usertofollow.following.remove(request.user.id)
    return HttpResponseRedirect(reverse('home'))
