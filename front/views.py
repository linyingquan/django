from django.http import HttpResponse
from django.shortcuts import redirect,reverse  # 跳转页面,反转

def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("前台首页")
    else:
        login_url = reverse('front:login')
        # print(login_url)
        return redirect(login_url)

def login(request):
    return HttpResponse("前台登录页面")
