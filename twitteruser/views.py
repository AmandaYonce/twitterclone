from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import render
from tweet.models import Tweet
from .models import *
from django.db.models import Q

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def Home(request):
    myfollowers = CustomUser.objects.get(id=request.user.id).followers.all()
    for each in myfollowers:
        followingTweets = Tweet.objects.filter(Q(author=request.user) | Q(author=each)).order_by('-timestamp')

    return render(request, 'home.html', { 'followingTweets': followingTweets})
