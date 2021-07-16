from bilibili_api import comment, sync
import re

async def main():
    # 存储评论
    comments = []
    pure_com = []
    pattern = re.compile(r'[(.*)]')
    # 页码
    page = 1
    # 当前已获取数量
    count = 0
    while True:
        # 获取评论
        c = await comment.get_comments(418788911, comment.ResourceType.VIDEO, page)
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
        if len(com) < 100 and '[' in com:
            pure_com.append(com)
    print(pure_com)
    # 打印评论总数



sync(main())