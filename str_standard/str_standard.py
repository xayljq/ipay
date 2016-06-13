#!/usr/bin/env python
# -*- coding: utf-8 -*-

from langconv import *

def strQ2B(ustring):#全角转半角
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:                              #全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248
        rstring += unichr(inside_code)
    return rstring

def str_standard(line):
	# 转换繁体到简体
	line = Converter('zh-hans').convert(strQ2B(line.lower().decode('utf-8')))
	line = line.encode('utf-8')

	return line.replace('\\', '').replace('/', '').replace(' ', '').replace('\t', '').strip()

	# 转换简体到繁体
	#line = Converter('zh-hant').convert(line.decode('utf-8'))
	#line = line.encode('utf-8')

if __name__ == '__main__':
	Str = "在GUIx。／線/i繁    體字\轉換,《器“:"
	print Str
	print str_standard(Str)
	for line in sys.stdin:
		print str_standard(line)

