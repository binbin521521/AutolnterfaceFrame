import unittest, requests
from api.login_api import LoginApi


class TestTPShopLogin(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        cls.session = requests.Session()
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_login_success(self):
        # 调用获取验证码
        response = self.login_api.get_verify(self.session)
        # 断言验证码是不是一个图片
        self.assertEqual("image/png", response.headers.get("Content-Type"))
        # 调用登陆接口
        data = {"username": "15839524016", "password": "123456", "verify_code": "8888"}
        response = self.login_api.login(data, self.session)
        # 获取登陆接口的返回的json数据
        jsonData = response.json()
        print("登陆接口的Json数据为：", jsonData)
        # 断言登陆接口
        self.assertEqual(200, response.status_code)  # 断言响应状态码
        self.assertEqual(1, jsonData.get('status'))  # 断言返回的json数据当中status的值
        self.assertEqual("登陆成功", jsonData.get('msg'))
        self.assertEqual("斌斌", jsonData.get('result').get('nickname'))

    def test02_logon_is_not_exists(self):
        # 获取验证码
        response = self.login_api.get_verify(self.session)
        # 断言验证码是不是一个图片
        self.assertEqual("image/png", response.headers.get("Content-Type"))
        # 调用登录接口
        data = {"username": "15839524026", "password": "123456", "verify_code": "8888"}
        response = self.login_api.login(data, self.session)
        # 断言
        # 断言响应状态码
        self.assertEqual(200, response.status_code)
        # 断言json中的status的值-1
        self.assertEqual(-1, response.json().get('status'))
        # 断言msg是'账号不存在！'
        self.assertIn("账号不存在!", response.json().get('msg'))

    def test03_password_is_wrong(self):
        # 获取验证码
        response = self.login_api.get_verify(self.session)
        # 断言验证码
        self.assertEqual("image/png", response.headers.get("Content-Type"))
        # 调用登录接口
        data = {"username": "15839524016", "password": "12345", "verify_code": "8888"}
        response = self.login_api.login(data, self.session)
        # 断言
        # 断言响应状态码
        self.assertEqual(200, response.status_code)
        # 断言json中的status的值-2
        self.assertEqual(-2, response.json().get('status'))
        # 断言msg是'账号不存在！'
        self.assertIn("密码错误", response.json().get('msg'))
