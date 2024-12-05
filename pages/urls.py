from django.urls import path
from . import views
from resumes.views import index

app_name = "pages"

urlpatterns = [
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path("", index, name="home"),

]