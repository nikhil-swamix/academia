import os
from mxproxy import mx
import re

def get_body(url,bodyclass=''):
	if bodyclass:
		return mx.get_page(url).find(class_=bodyclass)
	else:
		print('define bodyclass as parameter of this function')
	

if __name__ == '__main__':
	text=mx.fread('DIP MAIN.pdf.txt')
	text = re.sub(r'(-\n)|(\n\n)',' ',text)
	print(text)

