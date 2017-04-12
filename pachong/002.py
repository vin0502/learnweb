#! /user/bin/python3
# -*- coding:utf-8 -*-
# author: vin

#爬虫入门练习

import re
import urllib
import urllib.request
from collections import deque

queue = deque()
visited = set()


url = 'http://www.baidu.com/s?word=python'
queue.append(url)
cnt = 0

while queue:
	url = queue.popleft()  #队首元素出队
	visited |= {url}

	print('已经抓取：%d    正在抓取<---  %s' % (cnt, url))
	cnt += 1
	urlop = urllib.request.urlopen(url)
	if 'html'not in urlop.getheader('Contet-Type'):
 		continue
	try:
		data = urlop.read()
		data = data.decode('utf-8')
	except:
		continue

	linkre = re.compile('href="(.+?)"')

	for x in linkre.findall(data):
		print(x)
		if 'http' in x and x not in visited:
			queue.append(x)
			print('加入队列--->   '+ x)