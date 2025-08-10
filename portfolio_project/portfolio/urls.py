from django.urls import path
from . import views as this_is_portfolio

urlpatterns = [
    path('', this_is_portfolio.home, name='home'),
    path('about/', this_is_portfolio.about, name='about'),
    path('projects/', this_is_portfolio.projects, name='projects'),
    path('contact/', this_is_portfolio.contact, name='contact'),
]