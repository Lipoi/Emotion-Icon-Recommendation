import numpy as np
import re
pat1 = re.compile(r'\[(.*?)\]')
pat2 = re.compile(r'(.*?)\[')
s = '我好饿啊啊[哈哈]拉拉[露露]芜湖'
icon = re.search(pat1, s).group()
comment = re.search(pat2, s).group()
print(icon)
print(comment)