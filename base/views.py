from django.conf import settings
from django.shortcuts import render

from utils import set_cookie

def home(request):
    response = render(request, 'index.html')
    set_cookie(response, "STATIC_URL", settings.STATIC_URL, days_expire=7)
    return response
