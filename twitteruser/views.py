from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import render, HttpResponseRedirect
from tweet.models import Tweet
from .models import *
from notification.models import Notification


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def Home(request):
    if request.user.is_authenticated: 
        author = CustomUser.objects.get(id=request.user.id)
        myfollowers = author.followers.all()
        followingTweets=[]
        mytweets = Tweet.objects.filter(author=request.user)
        if mytweets:
            for myeach in mytweets:
                followingTweets.append(myeach)
        for each in myfollowers:
            ftweets = Tweet.objects.filter(author=each)
            if len(ftweets) > 0:
                for feach in ftweets:
                    followingTweets.append(feach)
        followingTweets = sorted(followingTweets, key=lambda k: (k.timestamp))
        count_notif = Notification.objects.filter(at_person=request.user.id, read=False).count()
        return render(request, 'home.html', {'followingTweets': followingTweets[::-1], 'count_notif': count_notif})
    return HttpResponseRedirect("/users/login/")
