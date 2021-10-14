# -*- coding:UTF-8 -*-
'''
网页打地鼠的外挂原理:request里有老鼠的位置 ,然后自己模拟post的数据发给服务器
那个数据是通过抓包看出来的
'''


import json
import requests

isfirst = 0
autonum = "0"
host = "http://mpsw-blocktest-cloud.rnd.ki.sw.ericsson.se/mouse/index.jsp"
login_host = "http://mpsw-blocktest-cloud.rnd.ki.sw.ericsson.se/mouse/swcralogin.jsp"
game_host = "http://mpsw-blocktest-cloud.rnd.ki.sw.ericsson.se/mouse/beatmouse.html"
hit = "http://mpsw-blocktest-cloud.rnd.ki.sw.ericsson.se/mouse/dohits"
start = "http://mpsw-blocktest-cloud.rnd.ki.sw.ericsson.se/mouse/dostart"
uname = "EENHENI"
upswd = "Shadow**19921211"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q =0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://mpsw-blocktest-cloud.rnd.ki.sw.ericsson.se/mouse/index.jsp',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

game_headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Referer': 'http://mpsw-blocktest-cloud.rnd.ki.sw.ericsson.se/mouse/beatmouse.html',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'keep-alive'
}

s = requests.session()


def login():
    post_url = login_host
    post_data = "username="+uname+"&password="+upswd
    login = s.post(post_url, data=post_data, headers=headers)
    return login


def enter_game(login):
    post_url = game_host
    post_data = "language=chinese"
    game = s.post(post_url, data=post_data, cookies=login.cookies, headers=headers)
    return game


def start_game(game):
    post_url = start
    game = s.get(post_url, cookies=game.cookies, headers=game_headers)
    return game


def send_hit(click):
    post_url = hit
    # 如果不加判断会爆出错误：TypeError: Object of type 'bytes' is not JSON serializable
    if isinstance(click.content, bytes):
        data = json.dumps(str(click.content, encoding='utf-8'))
    # data = json.dumps(click.content)
    hitnum = data[data.find(":")+1:data.find(",")-1]
    global autonum
    if isfirst:
        remian_data = data[data.find(",")-1:]
        tautonum = remian_data[remian_data.find(":")+1:remian_data.find("}")]
        autonum = tautonum
    post_data = "beat=" + hitnum + "&autonum=" + autonum
   # print(post_data)
    game = s.post(post_url, data=post_data, cookies=click.cookies, headers=game_headers)
    return game


if __name__=="__main__":
    isfirst = 1
    r = login()
    game = enter_game(r)
    sg = start_game(game)
    #print sg.content
    ret = send_hit(sg)
    isfirst = 0
    while (ret.content):
        ret = send_hit(ret)
        #print ret
