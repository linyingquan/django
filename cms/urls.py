from django.urls import path
from . import views

# 应用命名空间
app_name = 'cms'

urlpatterns = [
    path ('', views.index, name='index'),
    path ('login/', views.login, name='login')
]