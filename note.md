# Django学习笔记
## 一. python虚拟环境配置

1. 安装python虚拟环境生成器
    - 使用 pip install virtualenvwrapper-win 安装python虚拟环境生成器
2. virtualenv基本使用
    - 创建虚拟环境
    `kvirtualenv my_env`
    - 切换虚拟环境
    `workon my_env`
    - 退出当前虚拟环境：
    `deactivate`
    - 删除某个虚拟环境：
    `rmvirtualenv my_env`
    - 列出所有虚拟环境：
    `lsvirtualenv`
    - 进入到虚拟环境所在的目录：
    `cdvirtualenv`
3. 修改 mkvirtualenv 的默认路径：
    - 在 我的电脑->右键->属性->高级系统设置->环境变量->系统变量 中添加一个参数 `WORKON_HOME` ，将这个参数的值设置为你需要的路径
4. 创建虚拟环境的时候指定 Python 版本：
    - 在使用 mkvirtualenv 的时候，可以指定 --python 的参数来指定具体的 python 路径：`mkvirtualenv --python==C:\Python36\python.exe hy_env`
    
### 1.1 环境安装
1. Pycharm安装
    http://www.runoob.com/w3cnote/pycharm-windows-install.html
2. Mysql的安装
    https://blog.csdn.net/Night2233/article/details/88859405
    - 排错：
    https://www.sohu.com/a/227127720_100098990
    https://blog.csdn.net/liuyi6/article/details/81367407
   
### 1.2 项目运行
1. cmd运行命令：`python manage.py runserver 0.0.0.0:9000` 其他可访问，不加`0.0.0.0:9000` 默认是本机ip和`8000`端口号
2. Pycharm是点击右上角运行，更改IP和端口号则是更改设置即可
3. 在setting.py文件中更改 `ALLOWED_HOSTS = [‘本机IP’]`，注意需要打开本机防火墙

### 1.3 目录结构
1. `manage.py` ：以后和项目交互基本上都是基于这个文件。一般都是在终端输入 python
manage.py [子命令] 。可以输入 `python manage.py help` 看下能做什么事情。除非你知道你自
己在做什么，一般情况下不应该编辑这个文件。
2. `settings.py` ：本项目的设置项，以后所有和项目相关的配置都是放在这个里面。
3. `urls.py` ：这个文件是用来配置URL路由的。比如访问 http://127.0.0.1/news/ 是访问新闻
列表页，这些东西就需要在这个文件中完成。
4. `wsgi.py` ：项目与 WSGI 协议兼容的 web 服务器入口，部署的时候需要用到的，一般情况下
也是不需要修改的。

### 1.4 视图函数
1. 视图一般都写在 app 的 views.py 中。并且视图的第一个参数永远都是 request （一个
HttpRequest）对象。
2. 视图函数的返回结果必须是 HttpResponseBase 对象或者子类的对象。
    
        from django.http import HttpResponse
        def book_list(request):
        return HttpResponse("书籍列表！")
        
- url映射

    视图写完后，要与URL进行映射，也即用户在浏览器中输入什么 url 的时候可以请求到这个视图
函数。在用户输入了某个 url ，请求到我们的网站的时候， django 会从项目的 `urls.py` 文件中
寻找对应的视图。在 `urls.py` 文件中有一个 `urlpatterns` 变量，以后 django 就会从这个变量中
读取所有的匹配规则。匹配规则需要使用 `django.urls.path` 函数进行包裹，这个函数会根据传入
的参数返回 `URLPattern` 或者是 `URLResolver` 的对象。示例代码如下：
    ```
    from django.contrib import admin
    from django.urls import path
    from book import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path ('book/', views.book),
        path ('book/deta/<book_id>/', views.book_deta), # 变量传递方式
        path ('book/author/', views.author_deta)        # 字符串查询方式
    ]

    ```
    
- url传参数

    在 path 函数中，使用尖括号的形式`<参数名>`来定义一个参数。比如我现在想要获取一本书籍的详细信息，那么应该在 url 中指定这个参数。
    也可以通过查询字符串的方式传递一个参数过去。示例代码如下：
    ```
    def book_deta(request, book_id):          # 使用变量的方式
        text = " id为：%s" % book_id
        return HttpResponse(text)

    def author_deta(request):
        author_id = request.GET.get('id')      # 查询字符串方式
        text = 'author id is : %s' % author_id
        return HttpResponse(text)

    ```
    
### 1.5 url命名
1. 因为url是经常变化的，为避免写死url而大量更改代码，所以要给url取个名字，在使用的时候就使用它的名字进行反转就可以了
2. 如何指定url的名称
    - 在`path`函数中，传递一个`name`参数就可以指定，示例代码：
    ```
    urlpatterns = [
       path ('', views.index, name='index'),
       path ('login/', views.login, name='login')
    ]
    ```
3. 应用命名空间
    
    - 在多个app之间，可能产生同名的url，为避免反转url的时候产生混淆，可以使用应用命名空间来区分
    - 定义应用命名空间非常简单，只需要在`urls.py`中定义一个`app_name`的变量即可,示例代码如下：
    ```
    from django.urls import path
    from . import views

    # 应用命名空间
    app_name = 'front'

    urlpatterns = [
        path ('', views.index, name='index'),
        path ('login/', views.login, name='login')
    ]
    ```
    
    - 在反转url的时候就可以使用`应用命名空间：url名称`的方式进行反转