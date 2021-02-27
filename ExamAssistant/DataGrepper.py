import os
from mxproxy import mx
import re

def get_body(url,bodyclass=''):
	if bodyclass:
		return mx.get_page(url).find(class_=bodyclass)
	else:
		print('define bodyclass as parameter of this function')
	

if __name__ == '__main__':
	SUBJECTFOLDER='SEM-5/DIP/'
	url='https://www.sanfoundry.com/1000-digital-image-processing-questions-answers/'
	page=mx.get_page_soup(url)

	links={x['href'] for x in page.select('.entry-content a')}

	mx.touch(SUBJECTFOLDER+'visited.url')
	visited=mx.setload(SUBJECTFOLDER+'visited.url')

	pendinglinks=links - visited
	for x in pendinglinks:
		text=mx.get_page_soup(x).select_one('.entry-content').text
		mx.fappend('SEM-5/DIP/BigData.txt',text)
		mx.fappend(SUBJECTFOLDER+'visited.url',x)
		# print(text)
