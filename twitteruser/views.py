from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import render
from tweet.models import Tweet


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def Home(request):
    tweets = Tweet.objects.all()
    mytweets = Tweet.objects.filter(author=request.user.id)
    return render(request, 'home.html', {'tweets': tweets, 'mytweets': mytweets})
