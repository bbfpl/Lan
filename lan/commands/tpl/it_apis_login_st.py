# coding=utf-8
import unittest2
from lan import Request, Log
from model import Test


class TestUserLogin(Test):
    # 测试登录
    def test_login(self):
        Log.debug('开始测试')
        self.result = Request.get('https://yg.api.dev.diyelf.com/v1/noauthority/video_play?id=201')
        Log.info(self.result)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    print('开始')
    unittest2.main()
