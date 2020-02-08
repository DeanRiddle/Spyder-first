# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 17:07:23 2019

@author: Dean
"""
import xs

num=2206
adds='https://www.pingshu8.com/down_'
path='E:/pingshu/fl/'
name='大河风流'
i=31
steps=70
for n in range(num,num+steps):
    str3=adds+str(n)+'.html'
    try:
        str1=xs.path(str3)
    except Exception as ex:
        print('again \n')
        f=open(path+'err.log','w+')
        f.write('No.'+str(i)+':'+str(ex)+'\n')
        f.write(str1+'\n')
        f.close()
        str1=xs.path(str3)
    str2=path+name+xs.renamed(str(i))+'.mp3'
    xs.down_load(str1,str2)
    i=i+1
