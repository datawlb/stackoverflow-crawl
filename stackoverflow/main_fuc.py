# -*- coding:utf-8 -*-
__author__ = 'datawlb'
import json
import urllib2
import numpy
import pylab

data_dic = {}
count = 0
with open('stackoverflow.json') as f:
    for line in f:
        count +=1
        for elem in json.loads(line)['key'].split(' '):
            if elem in data_dic:
                data_dic[elem] += 1
            else:
                data_dic[elem] = 1
        #data.append(json.loads(line))

        print(len(data_dic))
#data = json.load('stackoverflow.json')
data_dic = sorted(data_dic.iteritems(), key=lambda data_dic:data_dic[1],reverse=True)

keylist = []
vallist = []
for i in range(20):
    keylist.append(data_dic[i][0])
    vallist.append(data_dic[i][1])

barwidth=1
xVal=numpy.arange(len(keylist))
pylab.xticks(xVal+barwidth/2.0,keylist,rotation=45)
pylab.bar(xVal,vallist,width=barwidth,color='y')
pylab.title(u'stackoverflow language rankings--'+ str(count) + ' recent records')
pylab.show()

print(len(data_dic))


