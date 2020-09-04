from django.urls import path, include
from . import views
from .views import SignUpView


urlpatterns = [
    path('', views.Home, name="home"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('/users/', include('django.contrib.auth.urls'))
]