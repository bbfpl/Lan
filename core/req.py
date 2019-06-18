# coding=utf-8
import requests


class Req:
    def __header(self, token):
        # print('headers')
        return token

    # get
    @classmethod
    def _get(cls, api, params, headers):
        r = requests.get(api, params=params, headers=headers, stream=True)
        return r

    # post
    @classmethod
    def _post(cls, api, data, headers):
        r = requests.post(api, data=data, headers=headers, stream=True)
        return r

    # request
    @classmethod
    def request(cls, api='', type="post", data={}, headers={}):
        # 根据type
        if type == 'get':
            r = cls._get(api, data, headers)
        elif type == 'post':
            r = cls._post(api, data, headers)
        else:
            print('没有找到')


        r_data = {
            'status_code': 0,
            'status': '',
            'response': {},
            'time': 0,  # 时间
            'msg': ''  # 错误提示
        }

        if r.status_code == 200:
            r_data['response'] = r.json()
            r_data['status'] = 'success'
        else:
            r_data['status'] = 'error'
            r_data['msg'] = r.text

        r_data['time'] = r.elapsed.total_seconds()
        r_data['status_code'] = r.status_code

        return r_data


if __name__ == '__main__':
    print('测试模块功能')
