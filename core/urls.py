from django.urls import path, include
from core.views import FacebookLogin, GithubLogin

urlpatterns = [
    path('auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('auth/github/', GithubLogin.as_view(), name='github_login'),
]