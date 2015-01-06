#coding=utf-8
__author__ = 'Hong' + " Chris"
import os
import re
import urllib2
import urllib


class HttpResource:

    all_http_url = r'"(https?://.*?)"'
    all_sub_url = r'"\/\/?(.*?)"'

    def __init__(self, url):
        self.url = url

    def get_1st_source(self):
        try:
            myRequest = urllib2.urlopen(self.url, None, 5)
            content = myRequest.read()
            if content:
                return content
        except:
            print 'http request error'

    def get_all_url(self):
        url_list = []
        content = self.get_1st_source()
        http_1 = re.findall(self.all_http_url, content)
        for i in http_1:
            url_list.append(i)

        http_2 = re.findall(self.all_sub_url, content)
        for j in http_2:
            url_list.append(self.url + j)

        url_list = list(set(url_list))

        for i, j in enumerate(url_list):
            if ".png" in j or ".jgp" in j:
                print 'downloading: ', j
                urllib.urlretrieve(j, 'D:/F/' + str(i) + '.png')

c = HttpResource('https://octodex.github.com/')
c.get_all_url()