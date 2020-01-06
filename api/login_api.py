class LoginApi:
    def __init__(self):
        self.verify_url = "http://127.0.0.1/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://127.0.0.1/index.php?m=Home&c=User&a=do_login"

    def get_verify(self, session):  # session 外部传入的session 实例：session = requests.Session() 初始化的实例
        # 为什么要从外部传入session
        # 因为可以在外部控制传入的session实例，从而确保每个session都相同
        # 发送获取验证码结果，获取响应数据
        response = session.get(self.verify_url)
        # 返回验证码接口的响应数据，包括状态行，响应头和响应体，返回的是一个requests.Response对象
        return response

    def login(self, data, session):  # data 外部传入的登录数据，session外部传入的session 实例 ，
        # 发送登录接口请求
        response = session.post(self.login_url, data=data)
        # 返回调用登录接口的响应数据
        return response
