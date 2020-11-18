import requests
'''
get请求：带参数
url = "https://www.baidu.com"
payload = {'username':'admin','password':'admin'}
r = requests.get(url,params=payload)
result = r.content
#print(r.status_code)

#post请求
url = "http://dvwa.bihuo.cn/login.php"

data = {'username':'admin','password':'admin'}
r = requests.post(url,data=data)
print(r.status_code)
#print(type(r.text))
if r.text.find('fail'):
    print('admin:admin'+' fail')
'''
#自定义请求头
url = "http://dvwa.bihuo.cn/login.php"

headers = {"User-Agent":"HAHA"}
r = requests.get(url,headers=headers)
print(r.request.headers)