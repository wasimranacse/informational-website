from django.urls import path
from .views import (
    HomePageView, AboutPageView, ServicePageView,
    DevTeamPageView, ContactPageView
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('about-us/', AboutPageView.as_view(), name='about-us'),
    path('our-services/', ServicePageView.as_view(), name='our-services'),
    path('developer-team/', DevTeamPageView.as_view(), name='developer-team'),
    path('contact-us/', ContactPageView.as_view(), name='contact-us'),

]