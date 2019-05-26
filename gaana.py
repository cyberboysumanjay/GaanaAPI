#Old Handler
from bs4 import BeautifulSoup
import requests
import lxml
#New Handler
from Crypto.Cipher import AES
import re
import sys
import os
import argparse
from json import JSONDecoder
from traceback import print_exc
import m3u8
import base64
import subprocess
import json
#Add Metadata
import eyed3
import lyricwikia
unpad = lambda s : s[0:-ord(s[-1])]
REGEX = re.compile('> ({[^<]*}) <')
JSONDEC = JSONDecoder()
DOWN_FOLDER = '.'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
}

def fate_proxy():
    resp=requests.get('https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list')
    a=((resp.text).split('\n'))
    p_list=[]

    for i in a:
        try:
            p_list.append(json.loads(i))
        except Exception as e:
            #print("Test",e)
            continue
    #print(len(p_list))
    np_list=[]
    for i in p_list:
        if i['country']=='IN':
            np_list.append(i)
    proxy=[]
    for i in np_list:
        proxy.append((str(i['host'])+':'+str(i['port'])))
    return(proxy)

def fix_share_url(s):
    s=s.replace("\\",'')
    s='https://gaana.com'+s
    return (s)

def decryptLink(message):
    IV = 'asd!@#!@#@!12312'.encode('utf-8')
    KEY = 'g@1n!(f1#r.0$)&%'.encode('utf-8')
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    #message=message.encode('utf-8')
    return unpad((aes.decrypt(base64.b64decode(message))).decode('utf-8'))

def fix_artist_name(t):
    t=t.split(',')
    l=[]
    for i in t:
      i=i.split('#')[0]
      l.append(i)

    singers=''
    for i in l:
      singers=singers+i+', '
    singers=singers[:len(singers)-2]
    return singers

def downloadAndParsePage(link):
    response=''
    response=requests.get(link,headers=headers).text
    raw_songs = list(set(REGEX.findall(response)))
    #print(raw_songs)
    if len(raw_songs)==0:
        try:
            proxies=fate_proxy()
            #print(proxies)
            for proxy in proxies:
                try:
                    response = requests.get(link,headers=headers,proxies={"http": proxy, "https": proxy}).text
                    #print(response)
                    break
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

    raw_songs = list(set(REGEX.findall(response)))
    songs = []
    for raw_song in raw_songs:
        json_song = JSONDEC.decode(raw_song)

        enc_message = None
        try:
            if 'high' in json_song['path']:
                enc_message = json_song['path']['high'][0]
            elif 'medium' in json_song['path']:
                enc_message = json_song['path']['medium'][0]
            elif 'normal' in json_song['path']:
                enc_message = json_song['path']['normal'][0]
            else:
                enc_message = json_song['path']['auto'][0]


            song = {'title' : json_song['title'],
                    'album' : json_song['albumtitle'],
                    'thumb' : json_song['albumartwork_large'],
                    'language' : json_song['language'],
                    'gaana_url' : fix_share_url(json_song['share_url']),
                    'duration' : str(int(json_song['duration'])//60)+"min " + str(int(json_song['duration'])%60) + "sec",
                    'artist' : fix_artist_name(json_song['artist']),
                    'released' : json_song['release_date'],
                    'bitrate' : enc_message['bitRate'],
                    'link' : decryptLink(enc_message['message'])
            }
            songs.append(song)
        except Exception as e:
            print(e)
    return songs

#print(downloadAndParsePage('https://gaana.com/song/homicide-109'))
#fate_proxy()
