# -*- coding: utf-8 -*-
import core
import model
import settings

from bs4 import BeautifulSoup
import settings
import model
import misc
import shlib
import time
import datetime
#import urllib
import logging
import urllib.request
import core
import re




#针对近30天内的销售情况抓取

def getSeltInfoLastMonth(url):
    data_source = []
    info_dict = {}

    html = misc.get_source_code(url)
    soup = BeautifulSoup(html,'lxml')

    totalPrice = soup.find('span', class_='record_price').get_text()[:-1]
    unitPrice = soup.find('p',class_='record_detail').get_text().split(',')[0][2:-3]
    dealdate = soup.find('p',class_='record_detail').get_text().split(',')[2]

    info_dict.update({'totalPrice':totalPrice})
    info_dict.update({'unitPrice': unitPrice})
    info_dict.update({'dealdate':dealdate})

    '''
    msg = soup.find('div',class_='msg').get_text()
    msgSplit = re.split(r'(\W+)',msg)
    guapaiPrince = msgSplit[0][:-4]
    chengjiaoZhouqi = msgSplit[4][:-4]
    adjustPriceCount = msgSplit[8][:-2]
    daikanCount = msgSplit[12][:-2]
    guanzhuCount = msgSplit[16][:-2]
    lookCount = msgSplit[20][:-2]

    '''
    msgSplit = soup.select('body > section.wrapper > div.overview > div.info.fr > div.msg > span > label')
    guapaiPrince = msgSplit[0].get_text()
    chengjiaoZhouqi = msgSplit[1].get_text()
    adjustPriceCount = msgSplit[2].get_text()
    daikanCount = msgSplit[3].get_text()
    guanzhuCount = msgSplit[4].get_text()
    lookCount = msgSplit[5].get_text()


    info_dict.update({'guapaiPrice':guapaiPrince})
    info_dict.update({'chengjiaoZhouqi':chengjiaoZhouqi})
    info_dict.update({'adjustPriceCount':adjustPriceCount})
    info_dict.update({'daikanCount':daikanCount})
    info_dict.update({'guanzhuCount':guanzhuCount})
    info_dict.update({'lookCount':lookCount})

    '''有问题
    baseInfo = soup.find('div', class_='content').get_text().split()
    buildYears = baseInfo[8][4:]
    warmStyle = baseInfo[11][4:]
    propertyRight = baseInfo[13][4:]
    '''
    baseInfo = soup.find('div', class_='content').findAll('li')
    buildYears = baseInfo[7].get_text()[4:].strip()
    warmStyle = baseInfo[10].get_text()[4:].strip()
    propertyRight = baseInfo[12].get_text()[4:].strip()



    info_dict.update({'buildYears':buildYears})
    info_dict.update({'warmStyle':warmStyle})
    info_dict.update({'propertyRight':propertyRight})

    data_source.append(info_dict)

    return data_source


if __name__ == "__main__":
    url = 'https://tj.lianjia.com/chengjiao/101102228368.html'

    res = getSeltInfoLastMonth(url)














