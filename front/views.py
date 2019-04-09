from django.http import HttpResponse
from django.shortcuts import redirect,reverse,render  # 跳转页面,反转
from django.template.loader import render_to_string

def index(request):
    context = {
        'books':[
            {
                'name':'lyq',
                'age':'18'
            },
            {
                'name':'csy',
                'age':'19'
            }
        ]
    }
    return render(request, 'index.html',context=context)


# class Person(object):
#     def __init__(self,username):
#         self.username = username
#
# def index(request):
#     # html = render_to_string("index.html")
#     # return HttpResponse(html)
#     # p = Person("林应权")
#     context = {
#         'persons':[
#             '林应权',
#             'javis',
#             'cuisyang'
#         ]
#     }
#     return render(request,'index.html', context=context)


# def index(request):
#     username = request.GET.get('username')
#     if username:
#         return HttpResponse("前台首页")
#     else:
#         login_url = reverse('front:login')
#         # print(login_url)
#         return redirect(login_url)
#
# def login(request):
#     return HttpResponse("前台登录页面")
