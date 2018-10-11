# -*- coding: utf-8 -*-
# 注意按照要求修改ID和FLAG
# ID{5771, 2116, 3684, 861777, 1058228; 9621, 1007170, 10199, 7760, 1024308}
import requests
import re
import os
import json
from bs4 import BeautifulSoup
import urllib

# 歌手号
ID = 0
# 文件编号
FLAG = 81
# 定制header
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)'
                  ' AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15'
}


# 返回该歌手页面的内容
def get_html(url):
    response = requests.get(url, headers=headers)
    # .content返回的是bytes型也就是二进制的数据(图片、文件)
    html = response.content
    return html


# 通过单曲id进入歌词页面并解析，返回歌词内容
def get_lyrics(music_id):
    # 歌词链接
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(music_id) + '&lv=1&kv=1&tv=-1'
    # .text返回的是Unicode型的数据(文本)
    response = requests.get(lrc_url)
    json_obj = response.text
    j = json.loads(json_obj)
    # 正则化
    lrc = j['lrc']['lyric']
    pat = re.compile(r'\[.*\]')
    lrc = re.sub(pat, "", lrc)
    lrc = lrc.strip()
    return lrc


# 下载音频
def get_song(music_id):
    song_url = 'http://music.163.com/song/media/outer/url?id=' + str(music_id) + '.mp3'
    os.chdir('/Users/lixinhao/Desktop/' + str(ID) + '音频')
    urllib.urlretrieve(song_url, str(FLAG) + '.mp3')


def download():
    global FLAG
    # https://music.163.com/#/artist?id=5771是歌手许嵩的网站
    # https加密，http超文本，这里不使用加密
    singer_url = 'http://music.163.com/artist?id={}'.format(ID)
    r = get_html(singer_url)
    # lxml -> HTML解析器解析快
    soup = BeautifulSoup(r, 'lxml')
    # 使用find方法查到第一个textarea标签，在textarea中保存了相关信息
    songs = soup.find('textarea').text

    # 将str类型的数据转成dict，解析json文件
    obj = json.loads(songs)
    # {}代表dict字典数据类型，字典是由键对值组组成；冒号':'分开键和值，逗号','隔开组
    # []代表list列表数据类型，列表是一种可变的序列
    # ()代表tuple元组数据类型，元组是一种不可变序列

    for item in obj:
        if FLAG <= 90:
            print (item['id'])
            print (item['name'])
            print (item['album']['picUrl'])

            # 将音频写入文件
            get_song(item['id'])

            # 将图像写入文件
            os.chdir('/Users/lixinhao/Desktop/' + str(ID) + '图像')
            urllib.urlretrieve(item['album']['picUrl'], str(FLAG) + '.png')

            # 将歌词写入文件
            os.chdir('/Users/lixinhao/Desktop/' + str(ID) + '歌词')
            text = get_lyrics(str(item['id']))
            my_file = open(str(FLAG) + '.txt', 'a')
            # 这一行需要格式转换
            my_file.write(u' '.join(item['name']).encode('utf-8') + '\n')
            my_file.write(text.encode('utf-8'))
            my_file.close()

            FLAG = FLAG + 1


# 进入主程序，输入歌手id下载Top10单曲及相关内容
if __name__ == '__main__':
    ID = 7760
    os.mkdir('/Users/lixinhao/Desktop/' + str(ID) + '音频')
    os.mkdir('/Users/lixinhao/Desktop/' + str(ID) + '歌词')
    os.mkdir('/Users/lixinhao/Desktop/' + str(ID) + '图像')
    download()
