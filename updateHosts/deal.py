#coding:utf-8
import os
import sys
import io
from urllib2 import urlopen


url = "https://hostsx.googlecode.com/svn/trunk/HostsX.orzhosts"
content = urlopen(url).read()
pos = content.find('version=')
end = content.find(";",pos)
print content[pos+8:end]
temp = open('hosts','w')
temp.write(content)
temp.close()


