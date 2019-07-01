# coding=utf-8
import unittest2
from lan import Test


class Login(Test):
    # 测试登录
    def get_token(self):
        r = self.request(self.data['url'], type=self.data['mode'])
        self.assertEqual(1, 1)


# 运行
if __name__ == '__main__':
    unittest2.main()
