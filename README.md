# Lan(懒)是一套测试框架 .

### 主要功能
接口测试(Interface Testing) 简称 it
服务器监控(Server monitoring) 简称 sm

### 安装
第一种 
https://pypi.org/project/lan.io/
```python
pip install lan
```
第二种 使用时可以直接下载源码来执行
```python
python setup.py install
```
### 使用方法
1、创建Project(自定义)文件夹,进入目录
```shell
cd Project
```
2、执行
```shell
lan
```
后显示
```
usage: lan [-h] {create,make,run,server} ...
Lan(懒)是一套Python测试套件脚手架
positional arguments:
  {create,make,run,server}
    create              - 创建项目 项目类型(it st sm)/项目名称
    make                - 用例生成 根据config.yaml文件生成用例文件
    run                 - 运行项目 结束退出
    server              - 运行项目 后台模式
```
3、选择需要创建的类型
创建接口测试(项目名称必填)：
```
lan create it/projectName
```
创建压测(项目名称必填)：
```
lan create st/projectName
```
创建服务器监控(项目名称必填)：
```
lan create sm/projectName
```
3、运行
```shell
python run.py
```

### 方法调用说明
```shell
# 需要模块哪些就引入哪些
from lan import Utils,Request,FileDb,Config,Log,Monitor
```
##### Utils 工具类
```
# 获取年月日
Utils.time_ymd()
# 返回：20190520
```
```
# 判断是否为空
Utils.empty(val)
# 返回：True/False
```
```
# 创建目录
Utils.mkdir(path)
# 返回：True/False
```
```
# 读取文件
Utils.open_file(path)
# 返回：content
```
```
# 写入文件
Utils.write_file(path, content)
```
```
# 删除文件
Utils.remove_file(path)
```

##### Request 请求类

```
# Get请求
Request.get(api,data,headers,stream)
```
```
# Post请求
Request.post(api,data,headers,stream)
```
```
# Put请求
Request.put(api,data,headers,stream)
```
```
# Delete请求
Request.delete(api,headers,stream)
```
统一返回
```
{
	'status_code': 200,
	'status': 'success', # success/error
	'response': {},
	'time': 0,  # 时间
	'msg': ''  # 错误提示
}
```




# 学习怎么开发框架
[开始学习](https://github.com/bbfpl/Lan/blob/master/doc/0.md "开始学习")
