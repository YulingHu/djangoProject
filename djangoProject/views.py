from datetime import datetime, timedelta

from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        userinfo = request.POST.dict()
        # userinfo.pop('csrfmiddlewaretoken')
        username = userinfo.get('username')
        password = userinfo.get('password')
        if username == 'aaa':
            response = redirect('/')
            future = datetime.now() + timedelta(days=3)
            response.set_cookie('username', username, expires=future)
            return response
    return render(request, 'login.html')