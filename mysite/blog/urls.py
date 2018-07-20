from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('archive', views.archive),
    path('tags', views.tags),
    path('about', views.about),
    path('<int:id>', views.details, name="blog_detail"),

]
