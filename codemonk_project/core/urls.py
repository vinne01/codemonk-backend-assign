from django.urls import path
from .views import RegisterUserView, CustomAuthToken, SubmitParagraphView, SearchParagraphView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('login/', CustomAuthToken.as_view()),
    path('submit/', SubmitParagraphView.as_view()),
    path('search/', SearchParagraphView.as_view()),
]
