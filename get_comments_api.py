from bilibili_api import comment, sync
import re
import codecs
import requests
import numpy as np
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
    pattern = re.compile(r'\[(.*?)\]')
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
        if len(com) < 200 and len(pattern.findall(com)) != 0:
            pure_com.append(com)
        #print(pattern.findall(com))
    # 打印评论总数
    return pure_com
'''
def get_com():
    comment = sync(main())
    return comment
'''
#comment = sync(main())
#np.savetxt('data.txt', comment, fmt="%s", encoding='utf-8') #保存为整数