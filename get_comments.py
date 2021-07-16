import requests
import json
import codecs

# import pprint

def bv2av(bvid):
    site = "https://api.bilibili.com/x/web-interface/view?bvid=" + bvid
    lst = codecs.decode(requests.get(site).content, "utf-8").split("\"")
    if int(lst[2][1:-1]) != 0: return "视频不存在！"
    return int(lst[16][1:-1])

BV = "BV1ab4y1k7A1"

AV = bv2av(BV)
coll = {}

url = "https://api.bilibili.com/x/v2/reply?&jsonp=jsonp&pn=1&type=1&oid={}&sort=2&_=1612337407736".format(AV)
data = json.loads(requests.get(url).text)
for i in data["data"]['replies']:
    coll[i['member']["uname"]] = i["content"]["message"]
comments = []
for value in coll.values():
    if len(value) < 100:
        comments.append(value)
print(comments)