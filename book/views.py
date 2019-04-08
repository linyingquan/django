from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def book(request):
    return HttpResponse("林应权")

def book_deta(request, book_id):          # 使用变量的方式
    text = " id为：%s" % book_id
    return HttpResponse(text)

def author_deta(request):
    author_id = request.GET.get('id')      # 查询字符串方式
    text = 'author id is : %s' % author_id
    return HttpResponse(text)