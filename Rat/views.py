from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
User = settings.AUTH_USER_MODEL


def home(request):
    return render(request, template_name='home.html')




