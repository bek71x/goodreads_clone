from django import views
from django.http import HttpResponse
from django.shortcuts import render


def landing_page(request):

    return  render(request,template_name='landingpage.html')
    # return HttpResponse(f"Django is working {request.META['HTTP_USER_AGENT']}")