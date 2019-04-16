import requests

# url为需要登录才能访问的个人主页地址
url = 'http://www.renren.com/967469305/profile'
# Cookie为登录成功后F12抓到的Request Headers
headers = {
	'Cookie': 'anonymid=ju0kshb9yeznc3; _r01_=1; depovince=BJ; JSESSIONID=abcb1lP3rVpdP67B8K6Nw; ick_login=42925146-a68e-4106-b250-82992bd13920; first_login_flag=1; ln_uact=13603263409; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20181101/1550/h_main_qz3H_61ec0009c3901986.jpg; jebe_key=1bd12da2-0649-43e0-8321-11b1bb27dee3%7C2012cb2155debcd0710a4bf5a73220e8%7C1554687212044%7C1%7C1554687212366; wp_fold=0; td_cookie=18446744070033157627; jebecookies=2eb13869-af73-48c8-a36e-c59c9d974a9a|||||; _de=4DBCFCC17D9E50C8C92BCDC45CC5C3B7; p=5b272ecf6801b5d160db5fe3aa5ad9965; t=34f7cff0d5a364c022197cf286ffca755; societyguester=34f7cff0d5a364c022197cf286ffca755; id=967469305; xnsid=5665706; loginfrom=syshome',
	'Referer': 'http://www.renren.com/SysHome.do',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
html = res.text

print(html)









