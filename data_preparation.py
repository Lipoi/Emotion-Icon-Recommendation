import get_comments_api
import re
import numpy as np
pattern = re.compile(r'\[(.*?)\]')

file = open("data.txt","r",encoding='utf-8')
list = file.readlines()
print(list)