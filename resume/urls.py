from django.urls import path
from .import views
from django.views.generic import TemplateView

urlpatterns = [
    path("",views.Home.as_view(),name="home"),
    path("templates",views.Templates.as_view(),name="templates"),
]
