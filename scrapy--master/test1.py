# -*- coding: utf-8 -*-
import os
import requests
import time

dirpath = r"D:\***"
filenames = os.listdir(dirpath)

jg = r'D:\***.txt'
fi = open(jg, 'w')
for filename in filenames:
    portion = os.path.splitext(filename)  # 将文件名和缀名分成俩部分
    if portion[1] == '.jpg' or portion[1] == '.png':
        filepath = os.path.join(dirpath, filename)

        # 接口
        url = 'https://***/***'
        files = {'topn': (None, '2'), 'image_file': ('file', open(filepath, 'rb'), 'image/jpeg')}
        r = requests.post(url, files=files)
        resp = r.json()
        print(resp)

        fi.write(str(filename) + ':' + str(resp) + '\n')
fi.close()