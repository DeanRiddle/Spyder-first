#引用 requests文件
import requests
import time
# -*-coding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#下载地址
#Download_addres='https://down01.pingshu8.xyz:8011/2/ps/%E5%BC%A0%E5%B0%91%E4%BD%90_%E7%A5%9E%E6%8E%A2%E7%8B%84%E4%BB%81%E6%9D%B0/%E5%BC%A0%E5%B0%91%E4%BD%90_%E7%A5%9E%E6%8E%A2%E7%8B%84%E4%BB%81%E6%9D%B0_02.mp3?t=c8685468aa560bfcbbaf42ffc2b34d211839c&m=5E2463E4'
#把下载地址发送给requests模块
#f=requests.get(Download_addres)
#下载文件
#with open("E:\\BaiduNetdiskDownload\\kk\\drj\\q.mp3","wb") as code:
#     code.write(f.content)

def down_load(address,name):
    f=requests.get(address)
#下载文件
    with open(name,"wb") as code:
        code.write(f.content)
    return

def path (pp):
    brower = webdriver.Firefox(executable_path='D:/Program Files/Mozilla Firefox/geckodriver.exe')
    brower.get(pp)
    brower.find_element_by_id('clickina').click()
    time.sleep(3)
    windows = brower.current_window_handle #定位当前页面句柄
    all_handles = brower.window_handles   #获取全部页面句柄
    for handle in all_handles:          #遍历全部页面句柄
        if handle != windows:          #判断条件
            brower.switch_to.window(handle)      #切换到新页面
    time.sleep(4)
    str1=brower.current_url
    brower.quit()
    if str1 == 'about:blank':
        raise Exception('address Exception')
    print(str1)
    return str1

def renamed(n_str):
    if len(n_str) ==1 :
        n_str = '00'+n_str
    elif len(n_str) ==2 :
        n_str = '0'+n_str
    return n_str