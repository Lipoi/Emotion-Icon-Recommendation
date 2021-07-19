import get_comments_api
import re
import numpy as np
from bilibili_api import sync
comments = sync(get_comments_api("BV1aK4y1P7Cg"))
pat1 = re.compile(r'\[(.*?)\]')
pat2 = re.compile(r'^\[(.*?)\]')
icon = re.search(pattern=pat, string=comments)