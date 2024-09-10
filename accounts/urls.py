from django.urls import include, path
from . import views
from .views import SignupView, SigninView, SignoutView, ChangePasswordView
urlpatterns = [
    path('', views.SignupView.as_view()),
    path('login/', views.SigninView.as_view()),
    path('logout/', views.SignoutView.as_view()),
    path('password/', ChangePasswordView.as_view()),
    path("<str:username>/", views.UserProfileView.as_view()),
]
