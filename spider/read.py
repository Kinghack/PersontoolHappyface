
#!/usr/bin/env python                                                          
#coding:utf-8
import pickle
con = ['america', 'europe', 'asia', 'oceania', 'africa']
for i in con:
    tmp = open(i,'r')
    dic = pickle.load(tmp)
    for i in dic.keys():
        print i#country name
        l = dic[i][1]
        for j in l:
            print j#city name
    tmp.close()
