content = '''
# 项目
project:
  # 当前项目配置文件
  config:
    # 域名
    domain: http://139.196.192.35:39001
    # 发送邮箱配置
    maile_host: null
    maile_port: null
    maile_user: null
    maile_passwd: null
    # 响应处理-可为空 如果为空就不判断响应后的字段
    response:
      # 状态字段 一般是code 或者 status
      status_field: status
      # 状态字段 正确 值
      status_success_val: success
      # 错误提示字段
      error_field: msg
    # 测试报告配置
    repore:
      title: 接口自动化测试报告
      cases:
        all: 全部
        success: 成功
        error: 错误
        skip: 跳过
      table:
        case_id: 用例编号
        case_name: 用例名称
        api_url: 接口地址
        method: 接口方法
        time: 时间
        result: 测试结果
        detailed: 详细信息

  # 所有用例模块配置
  models:
    #user模块
    user:
      # 登录 login_st.py
      login:
        className: TestUserLogin # 接口类名
        funName:
          # 接口方法名
          test_login:
            name: 登录 # 接口注释
            url: /api/login
            # 请求类型
            mode: post
            # 参数
            data:
              name: 15000000000
              password: 123
      # 获取所有用户 users_st.py
      users:
        className: TestUsers # 接口类名
        funName:
          # 接口方法名
          test_get_users:
            name: 登录 # 接口注释
            url: /api/get_users
            # 请求类型
            mode: get
      # 获取用户 user_st.py
      user:
        className: TestUser # 接口类名
        funName:
          # 接口方法名
          test_get_user:
            name: 登录 # 接口注释
            url: /api/get_user
            # 请求类型
            mode: get
            # 参数
            data:
              id: 1
'''


def get_yaml_tpl():
    return content


if __name__ == '__main__':
    print(get_yaml_tpl())
