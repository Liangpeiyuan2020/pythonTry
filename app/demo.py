# -*- codeing=utf-8-*-
# @Time: 2021/8/28 20:34
# @AUthor: BaBa
# @File: demo.py
# @software: PyCharm

import re
import requests
import bs4
import execjs

findSeq = re.compile(r'<td align="center" height="32px">(.*)</td>')
findCate = re.compile(r'<td align="center" style="font-size: 9pt"><a href="\?infotype=.*">(.*)</a></td>')
findApart = re.compile(r'<td align="center" style="font-size: 9pt"><a href=".*\sonclick.*>(.*)</a></td>')
findDate = re.compile(r'<td align="center" style="font-size: 9pt">(\d*-\d*-\d*)</td>')
findId = re.compile(r'<a class="fontcolor3" href="view.asp\?id=(\d*)')

def dataFilter(url):
    html = askURL(url)
    soup = bs4.BeautifulSoup(html, "html.parser")
    # print(soup)
    datalist = []

    for itemSeq in soup.find_all(attrs={"align": "center", "height": "32px"}):

        item = itemSeq.parent
        itemStr = str(item)

        seq = re.findall(findSeq, itemStr)[0]

        cate = re.findall(findCate, itemStr)[0]
        apart = re.findall(findApart, itemStr)[0]
        title = item.find(attrs={"class": "fontcolor3"}).string
        date = re.findall(findDate, itemStr)[0]
        tapCount = item.find(attrs={"title": "累计点击数"}).string
        id = re.findall(findId, itemStr)[0]


        datalist.append([seq, cate, apart, title, date, tapCount, id])

    return datalist
def askURL(url):

    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}
    session1 = requests.Session()
    session1.get("https://www1.szu.edu.cn/", headers=headers,verify=False)

    # 获取加密的password 开始
    crypt = session1.get("https://authserver.szu.edu.cn/authserver/custom/js/encrypt.js", headers=headers,verify=False).text
    encrypt = execjs.compile(crypt)  # 获取js加密代码
    print(encrypt)
    res = session1.get("https://authserver.szu.edu.cn/authserver/login", headers=headers,verify=False)  # 请求登录界面

    bs = bs4.BeautifulSoup(res.content, "html.parser")
    bs = bs.find_all('input', {'type': "hidden"})  # 寻找登录界面中需要的数据
    dist = {}
    for i in bs:
        try:
            dist[re.search('(?<=name=").*?(?=")', str(i)).group()] = re.search('(?<=value=").*?(?=")', str(i)).group()
        except:
            dist[re.search('(?<=id=").*?(?=")', str(i)).group()] = re.search('(?<=value=").*?(?=")', str(i)).group()

    username = '334834'
    password = 'xiao1999'
    enPassword = encrypt.call("encryptAES", password, dist["pwdDefaultEncryptSalt"])  # 利用js代码加密
    # print(enPassword)
    # 获取加密过的password 结束

    # 登录时需要POST的数据
    data = {
        "username": username,
        "password": enPassword,
        "lt": dist["lt"],
        "dllt": dist["dllt"],
        "execution": dist["execution"],
        "_eventId": dist["_eventId"],
        "rmShown": dist["rmShown"]
    }

    login_url = "https://authserver.szu.edu.cn/authserver/login?service=http%3A%2F%2Fwww1%2Eszu%2Eedu%2Ecn%2Fmanage%2Fcaslogin%2Easp%3Frurl%3D%2F"
    session1.post(login_url, headers=headers, data=data,verify=False)

    askRes2 = session1.get("https://www1.szu.edu.cn/board/infolist.asp", headers=headers, verify=False)

    askRes = session1.get("https://www1.szu.edu.cn/board/infolist.asp", headers=headers,verify=False)
    askRes.encoding = 'gbk'
    # print(askRes.text)
    return askRes.text
def main2():
    import warnings
    warnings.filterwarnings("ignore")

    baseurl = "https://www1.szu.edu.cn/board/infolist.asp"
    return dataFilter(baseurl)
# if __name__=="__main__":
#     sttr = main2()
    # saar = sttr[0]
    # saar = str(saar)
    # print(saar)
