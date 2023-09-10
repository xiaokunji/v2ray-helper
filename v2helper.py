import requests
import json
import time
import random

# 加入随机延时
time.sleep(random.randint(1, 30))

fromdata = {}
if fromdata == {}:
    fromdata['email'], fromdata["passwd"], sckey = input().strip().split(",")


# 微信推送
def send_wechat(content):
    # title and content must be string.
    title = "v2流量签到通知"
    url = 'https://sc.ftqq.com/' + sckey + '.send'
    data = {'text': title, 'desp': content}
    result = requests.post(url, data)
    return (result)


def main():
    print("准备发起请求....")
    s = requests.session()
    s.headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'w1.v2free.net',
        'Origin': 'https://w1.v2free.net',
        'Pragma': 'no-cache',
        'Referer': 'https://w1.v2free.net/auth/login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows'
    }
    url0 = f'https://w1.v2free.net/auth/login'
    try:
        r = s.get(url0, timeout=15)
    except requests.exceptions.RequestException as e:
        print("网页响应失败,请检查网站是否能正常访问", e)
        # send_wechat("网站响应失败")
        return

    try:
        r0 = s.post(url0, data=fromdata, timeout=15)
    except requests.exceptions.RequestException as e:
        print("登录失败...", e)
        # send_wechat("r0失败" + e)
        return
    if r0.status_code == 200:
        t = json.loads(r0.text)
        print(t['msg'])
    else:
        print("登录失败...", r0)
        # send_wechat("登录失败")

    print("开始签到...")
    url2 = f"https://w1.v2free.net/user/checkin"

    r2 = s.post(url2, timeout=15)
    r2.raise_for_status()
    t = json.loads(r2.text)
    if t["msg"]:
        print(t["msg"])
    else:
        print("签到失败", r2)
        # send_wechat("发生错误")
        exit(100)


if __name__ == "__main__":
    main()
