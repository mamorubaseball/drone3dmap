from django.urls import path
from . import views
from app.views import IndexView

app_name = 'app'
urlpatterns = [
    path('',IndexView.as_view(),name = ''),
]