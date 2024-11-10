from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User

def index(request):
    list = User.objects.all()
    return render(request, 'app/index.html', {'list': list})
