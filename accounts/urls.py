from django.urls import include, path
from . import views
from .views import SignupView, SigninView
urlpatterns = [
    path('signup/', views.SignupView.as_view()),
    path('signin/', views.SigninView.as_view()),
    path('signout/', views.SignoutView.as_view()),
    path("<str:username>/", views.UserProfileView.as_view()),
]
