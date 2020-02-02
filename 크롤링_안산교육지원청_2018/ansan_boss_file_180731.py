#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import bs4

url ="http://www.goeas.kr/USR/ORG/MNU1/Greeting.do"
html = urllib.request.urlopen(url)
bs_obj = bs4.BeautifulSoup(html, 'html.parser')

container = bs_obj.find('div',{'id':'main_container'})
boss_name = container.find('p',{'class':'name tr'})

# boss_name_text = boss_name.text
out = open('out.txt','w')
print(boss_name.text,file=out)
out.close()