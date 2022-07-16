from django.shortcuts import render
from .models import Userinfo
from django.views.generic import View
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'main/login.html')

    def post(self, request):
        id = request.POST['userid']
        pw = request.POST['userpw']
        msg = False

        infos=Userinfo.objects.all()
        for info in infos:
            if id == info.userid and pw == info.userpw:
                name = info.username
                msg = True
                break
        msg = name+"님 환영합니다."

        context={
            'msg' : msg,
        }
        return render(request, 'main/result.html', context)