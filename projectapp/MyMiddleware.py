from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

# from workapp.models import Regist
# from projectapp.models import TUser


class MyMiddleware(MiddlewareMixin):          # 自定义的中间件
    def __init__(self ,get_response)  :  # 初始化
        super().__init__(get_response)
        print("init1")

    # view处理请求前执行
    def process_request(self ,request):
        nickname = request.session.get('nickname')
        # print(nickname, '11515')
        if  'bookdetails' in request.path or 'booklist' in request.path or 'index' in request.path or 'register'in request.path or 'regis1321ter'in request.path:
            # print('123')
            if nickname:
                request.session['nickname1']=nickname
                # print(nickname,'1919')
            else:
                request.session['nickname1'] =''

    # 在process_request之后View之前执行
    def process_view(self ,request, view_func, view_args, view_kwargs):
        print("view:" ,request ,view_func ,view_args ,view_kwargs)

    # view执行之后，响应之前执行
    def process_response(self ,request ,response):
        print("response:" ,request ,response)
        return response  # 必须返回response

    # 如果View中抛出了异常
    def process_exception(self ,request ,ex)  :  # View中出现异常时执行
        print("exception:" ,request ,ex)