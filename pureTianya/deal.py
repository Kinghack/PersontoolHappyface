#coding:utf-8
import os
import sys
import io
import string
import codecs
import chardet
import time
from urllib2 import urlopen

FILENAME = 'paper.txt'

#find the url of next page
def find_url(begin, end, content):
       if type(content) is str:
              content = content.decode('utf-8')
       if not content:
              return ''
       start = content.find(begin)
       if start == 0:
              return None
       test = content.rfind('current"') 
       eee = content.find('href="',test)
       test = content.find('http',eee)
       eee = content.find('"',test)
       return content[test:eee].strip()


def txt_wrap_all(begin, end, url,num):
#可以用来控制不全部扫描，而只扫描前多少页面
#    if num > 5:
#         return
    num = num + 1
    content = urlopen(url).read()
    result = chardet.detect(content)
    content = content.decode('gbk','ignore')
    #content = content.decode(result['encoding'])
    content = content.encode('utf-8')
#    print content
    if type(content) is str:
           content = content.decode('utf-8')
    if not content:
           return ''
#    result = []
    from_pos = 0
    if num == 1:
          temp = open(FILENAME,'w')
    else:
          temp = open(FILENAME,'a')
    temp.write('')
    temp.close()
    while True:
        start = content.find(begin, from_pos)
        if start >= 0:
            start = start + len(begin)
            endpos = content.find(end, start)
            if endpos >= 0:
#                result.append(html[start:endpos].strip())
                temp = open(FILENAME,'a')
                temp.write(content[start:endpos].strip().encode('utf-8'))
                temp.close()
                #print html[start:endpos].strip().encode('utf-8') 
#                result = []
                from_pos = endpos+len(end)
                continue
        break
    label = '下一页'
    mark = '末页'
    label = label.decode('utf-8')
    mark = mark.decode('utf-8')
    url = find_url(label,mark,content)
    if url is None:
        return
    print url
    time.sleep(1)
    txt_wrap_all(begin,end,url,num)
    return 


#get content from web begin
#冒死记录
#url = "http://www.tianya.cn/techforum/content/16/1/627945.shtml"
#五大贼王
url = "http://www.tianya.cn/techforum/content/16/1/623828.shtml"
#get content from web end
#write to file begin
#temp = open("content",'w')
#temp.write(content)
#temp.close()
#write to file close

#content = open('content').read()
#print content 
        




#url = "http://www.tianya.cn/publicforum/content/free/1/2459458.shtml"
#url = "http://www.tianya.cn/techforum/content/16/1/623828.shtml"
#url = "http://www.tianya.cn/publicforum/content/university/1/309315.shtml"
begin = '作者：<a href="http://my.tianya.cn/368547" target="_blank">老夜</a>'
end = '<div class="post-jb">'
begin = begin.decode('utf-8')
end = end.decode('utf-8')
num = 0
#author = '美如天仙苹果姐'
#authorId = ''
#if authorId == '':
#       begin = '作者：<a href="http://my.tianya.cn/name/'+author+'" target="_blank">'+author+'</a>'
#else :
#       begin = '作者：<a href="http://my.tianya.cn/'+authorId+'" target="_blank">'+author+'</a>'
print begin
#begin = begin.decode('utf-8')
txt_wrap_all(begin,end,url,num)


