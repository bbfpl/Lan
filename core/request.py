# coding=utf-8
import requests


def _request(api='', method="get", data={}, headers={}, stream=True):
    if method == 'get':
        r = requests.get(api, params=data, headers=headers, stream=stream)
    elif method == 'post':
        r = requests.post(api, data=data, headers=headers, stream=stream)
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
        if r.headers.get('Content-Type') == 'text/html':
            # 获取html
            r_data['response'] = r.text.encode(r.encoding).decode()
        else:
            # 获取json
            r_data['response'] = r.json()

        r_data['status'] = 'success'
    else:
        r_data['status'] = 'error'
        r_data['msg'] = r.text

    r_data['time'] = r.elapsed.total_seconds()
    r_data['status_code'] = r.status_code

    return r_data


class Request:

    @staticmethod
    def get(api='', data={}, headers={}, stream=True):
        return _request(api, 'get', data, headers, stream)

    @staticmethod
    def post(api='', data={}, headers={}, stream=True):
        return _request(api, 'post', data, headers, stream)


if __name__ == '__main__':
    r = Request.get('http://baidu.com')
    print(r)
