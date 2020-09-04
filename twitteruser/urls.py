from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('', views.Home, name="home"),
    path('signup/', SignUpView.as_view(), name='signup'),
]