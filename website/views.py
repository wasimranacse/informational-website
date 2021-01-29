from django.shortcuts import render
from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = 'index.html'


class AboutPageView(generic.TemplateView):
    template_name = 'about_us.html'


class ServicePageView(generic.TemplateView):
    template_name = 'our_services.html'


class DevTeamPageView(generic.TemplateView):
    template_name = 'developer_team.html'


class ContactPageView(generic.TemplateView):
    template_name = 'contact_us.html'
