from bilibili_api import comment, sync
import re
import codecs
import requests
import numpy as np

import pandas as pd
# import pprint

def bv2av(bvid):
    site = "https://api.bilibili.com/x/web-interface/view?bvid=" + bvid
    lst = codecs.decode(requests.get(site).content, "utf-8").split("\"")
    if int(lst[2][1:-1]) != 0: return "视频不存在！"
    return int(lst[16][1:-1])
async def main(bvid):
    # 存储评论
    comments = []
    pure_com = []
    icon = []
    pat2 = re.compile(r'\[(.*?)\]')
    pat1 = re.compile(r'[^\[]+?\[')
    # 页码
    page = 1
    # 当前已获取数量
    count = 0
    while True:
        # 获取评论
        c = await comment.get_comments(bv2av(bvid), comment.ResourceType.VIDEO, page)
        # 存储评论
        comments.extend(c['replies'])
        # 增加已获取数量
        count += c['page']['size']
        # 增加页码
        page += 1

        if count >= c['page']['count']:
            # 当前已获取数量已达到评论总数，跳出循环
            break

    # 打印评论
    for cmt in comments:
        com = cmt['content']['message']
        if len(com) < 200 and com[0] != '[' and len(pat1.findall(com)) > 1:
            pure_com.append(re.search(pat1, com).group().replace("[", ""))
            icon.append(re.search(pat2, com).group())
        #print(pattern.findall(com))
    df = pd.DataFrame({'comments':pure_com,'icon':icon})
    df.to_csv(r"test.csv",sep=',')
    # 打印评论总数
'''
def get_com():
    comment = sync(main())
    return comment
'''
#comment = sync(main())
#np.savetxt('data.txt', comment, fmt="%s", encoding='utf-8') #保存为整数
sync(main("BV1aK4y1P7Cg"))