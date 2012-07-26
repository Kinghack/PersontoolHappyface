#!/usr/bin/env python                                                          
#coding:utf-8
import requests
import pickle

def getCity(link, country):
    r = requests.get(link)
    ci = []
    num = 1
    one = 0
    while(one >= 0):
        one = r.text.find(tabfive, one)
        if one < 0 :
            r = requests.get(link+'?page='+str(num))
            num += 1
            one = r.text.find(tabfive, 0)
            if one < 0 :
                break
            if num > 20:
                break
        two = r.text.find(tabsix, one)
        name = r.text[one+15:two-16]
        print country + name + '  ' + str(num)
        ci.append(name)
        one = two
    return ci

def getCountry(text, one, two):
    posone = 0
    country = {}
    while(posone >= 0):
        posone = text.find(one, posone)
        postwo = text.find(two, posone)
        if posone < 0:
            break
        ss = text[posone:postwo]
        start = ss.find('"')
        end = ss.find('"', start+1)
        link = url + ss[start+8:end] + 'explore/'
        print link
        name = ss[end+2:]
        city = getCity(link, name)
        print name
        #country[name] = link
        country[name] = (link, city)
        tmp = open(name, 'w')
        pickle.dump(country, tmp)
        tmp.close()
        posone = postwo
    tmp = open("all", "w")
    pickle.dump(country, tmp)
    tmp.close()
    #print country


def getContinent(text, one, two):
    posone = 0
    while(posone >= 0):
        posone = text.find(one, posone)
        postwo = text.find(two, posone)
        #test
        continent = text.rfind('place', posone)
        end = text.rfind('"', posone)
        print text[continent:end]
        print posone
        print postwo
        print continent
        print end
        break
        #end
        if posone < 0 :
            break
        getCountry(text[posone:postwo], tabthree, tabfour)
        posone = postwo
    return



url = 'http://tukeq.com/place/'

r = requests.get(url)


tabone = '<div class="nav-countries">'
tabtwo = 'div class="arrow-right'
tabthree = '<a href='
tabfour = '</a>'
tabfive = '<p class="t">'
tabsix = '</p>'

#a = {'two':'two'}
#tmp = open('英国', 'w')
#pickle.dump(a, tmp)
#tmp.close
#tmp = open('英国','r')
#dic = pickle.load(tmp)
#print dic['two']

getContinent(r.text, tabone, tabtwo)


