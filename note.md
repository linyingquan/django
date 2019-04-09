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

### 1.6 渲染模板
1. `render_to_string`:找到模板，然后将模板编译后渲染成python的字符串格式，然后通过HttpResponse类包装成一个HttpResponse对象返回出去，示例代码如下：
    ``` 
    from django.http import HttpResponse
    from django.template.loader import render_to_string

    def index(request):
        html = render_to_string("index.html")
        return HttpResponse(html)    
    ```
2. django还提供了更加简便的方式，直接将模板渲染成字符串和包装为HttpResponse对象一步到位，示例代码如下：
    ```
    from django.shortcuts import render 

    def index(request):
        return render(request,'index.html')
    ```
3. 模板查找路径配置  
    在项目的 settings.py 文件中。有一个 TEMPLATES 配置，这个配置包含了模板引擎的配置，模板
查找路径的配置，模板上下文的配置等。模板路径可以在两个地方配置。
    1. DIRS ：这是一个列表，在这个列表中可以存放所有的模板路径，以后在视图中使
22
知了课堂
用 render 或者 render_to_string 渲染模板的时候，会在这个列表的路径中查找模板。
    2. APP_DIRS ：默认为 True ，这个设置为 True 后，会在 INSTALLED_APPS 的安装了的 APP 下
的 templates 文件加中查找模板。
    3. 查找顺序：比如代码 render('list.html') 。先会在 DIRS 这个列表中依次查找路径下有没有
这个模板，如果有，就返回。如果 DIRS 列表中所有的路径都没有找到，那么会先检查当前这
个视图所处的 app 是否已经安装，如果已经安装了，那么就先在当前这个 app 下
的 templates 文件夹中查找模板，如果没有找到，那么会在其他已经安装了的 app 中查找。
如果所有路径下都没有找到，那么会抛出一个 TemplateDoesNotExist 的异常。

4. 向HTML模板传入参数
    ```
    def index(request):
       context = {'username':'林应权'}        # 通过字典的方式
       return render(request,'index.html', context=context)
    ```
    在HTML模板中接收参数
    ```
    <body>
        {{ username }}
    </body>
    ```
    如果定义的是一个class类，模板也可以通过.的方式访问它的属性
    ```
    class Person(object):
        def __init__(self,username):
            self.username = username
    def index(request):
        p = Person("林应权")
        context = {
            'person':p
        }
        return render(request,'index.html', context=context)
    ```
    html模板访问方式
    ```
    <body>
        {{ person.username }}
    </body>
    ```
    如果传入的参数为一个列表或元组的话
    ```
    def index(request):
        context = {
            'persons':[
                '林应权',
                'javis',
                'cuisyang'
            ]
        }
    html模板文件访问方式不能是[],而是.    
    ```
        <body>
            {{ persons.1 }}
        </body>

### 1.7 常用标签
1. `if`标签：与python类似，但是格式有变化，示例如下：
    ```html
    <body>
       {% if age < 18 %}
        <p>你是未成年</p>
       {% elif age == 18 %}
        <p>成年人</p>
       {% else  %}
        <p>害不害臊</p>
       {% endif %}
    </body>
    ```
    在`views.py`中的代码如下
    ```python
    def index(request):
       context = {
           'age': 18  # 传入的值
       }
       return render(request, 'index.html',context=context)
    ```
    在if标签中，==、!=、<、<=、>、>=、in、not，in、is、is not 等判断运算符都可以使用
    
2. `for...in...`标签：用法与python类似，常用于遍历等操作，没得back人，和countiue退出循环功能
    
    - 遍历列表：
    ```html
    <body>
       {% for username in usernames reversed %}  #加reversed反转遍历结果
           <li>{{ username }}</li>
       {% endfor %}
    </body>
    ```
    ```python
    def index(request):
    context = {
        'usernames': [
            '林应权',
            'javis',
            'cuishenyang'
        ]
    }
    return render(request, 'index.html',context=context)
    ```
    - 遍历字典：需要使用`item`，`keys`，`values` 等方法
    ```html
    <body>
        {% for username in usernames.items %}
           <li>{{ username }}</li>
        {% endfor %}
    </body>
    ```
    ```python
    def index(request):
    context = {
        'usernames': {
            'name': 'lyq',
            'age': 18,
            'head': 180
        }

    }
    return render(request, 'index.html',context=context)
    ```
    - 嵌套使用
    ```html
    <body>
    <ul>
        {% for book in books %}
            <li>{{ book.name }}</li>
            <li>{{ book.age }}</li>
        {% endfor %}
    </ul>
    </body>
    ```
    context数据：
    ```python
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
    ```
    - html表格基础
        - `<table>` : 表格
        - `<thead>` : 表头
        - `<tbody>` : 表格内容
        
    ```html
    <body>
        <table>
            <thead>
                <tr>
                    <td>序号</td>
                    <td>名字</td>
                    <td>年龄</td>
                </tr>
            </thead>
            <tbody>
                {% for book in books %}
                    <tr>
                        <td>{{ forloop.revcounter }}</td>
                        <td>{{ book.name }}</td>
                        <td>{{ book.age }}</td>
                    </tr>
                {% endfor %}
    
            </tbody>
        </table>
     </body>
    ```
    - forloop.counter 能够返回数字序号，默认从1开始，counter0是从0开始
    - forloop.revcounter 能够逆序返回数字序号
    - forloop.first ：是否是第一次遍历。
    - forloop.last ：是否是最后一次遍历。
    - forloop.parentloop ：如果有多个循环嵌套，那么这个属性代表的是上一级的for循环。
    ```html
       <tbody>
            {% for book in books %}
                {% if forloop.first %}
                    <tr style="background: red">    # 如果为第一行，则吧背景颜色设置为红色
                {% elif forloop.last %}
                    <tr style="background: pink">   # 如果为最后一行，则吧背景颜色设置为粉色
                {% else  %}
                    <tr>
                {% endif %}
                    <td>{{ forloop.revcounter }}</td>
                    <td>{{ book.name }}</td>
                    <td>{{ book.age }}</td>
                </tr>
            {% endfor %}
       </tbody>
    ```
3. `for...in...empty`标签，这个标签使用跟 for...in... 是一样的，只不过是在遍历的对象如果没有元素的情况下，会执行 empty 中的内容。示例代码如下：
    ```html
    {% for person in persons %}
       <li>{{ person }}</li>
    {% empty %}
       <li>暂时还没有任何人</li>   # 若person为空，则打印这一句
    {% endfor %}
    ```