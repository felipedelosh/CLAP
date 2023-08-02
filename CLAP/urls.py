from django.urls import path
from .views import CLAPCreateView

app_name="blog"

urlpatterns = [
    path('create/', CLAPCreateView.as_view(), name="create")
]