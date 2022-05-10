#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from tqdm import tqdm
import argparse
import os


class Video(object):

    def __init__(self, aweme_id, cover_links, music_links, video_links):
        self.__aweme_id = aweme_id
        self.__cover_links = cover_links
        self.__music_links = music_links
        self.__video_links = video_links
        # print(self.__aweme_id)
        # print(self.__cover_links)
        # print(self.__music_links)
        # print(self.__video_links)

    def __download_file(self, links, suffix):
        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
        }
        r = requests.get(links[0], headers=headers, stream=True)
        file_size = r.headers['Content-length']
        file_name = self.__aweme_id + suffix
        with tqdm.wrapattr(open('download/' + file_name, mode='wb'), "write", miniters=1, desc=file_name,
                           total=int(file_size)) as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)

    def download_all(self):
        self.download_video()
        self.download_cover()
        self.download_music()

    def download_cover(self):
        print('正在下载封面')
        self.__download_file(self.__cover_links, '.jpeg')

    def download_music(self):
        print('正在下载音乐')
        self.__download_file(self.__music_links, '.m4a')

    def download_video(self):
        print('正在下载无水印视频')
        self.__download_file(self.__video_links, '.mp4')


class Dyd(object):

    def __init__(self):
        pass

    @staticmethod
    def parse_link(share_link):
        api_url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='
        try:
            print('正在解析下载地址')
            r = requests.get(share_link)
            aweme_id = r.url.split('/')[-1]
            req_url = api_url + aweme_id
            headers = {
                'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
            }
            r = requests.get(req_url, headers=headers)
            result = r.json()
            cover_links = result['item_list'][0]['video']['origin_cover']['url_list']
            music_links = result['item_list'][0]['music']['play_url']['url_list']
            video_links = result['item_list'][0]['video']['play_addr']['url_list']
            video_links = list(map(lambda x: x.replace('playwm', 'play', 1), video_links))
            print('解析成功！')
            return Video(aweme_id, cover_links, music_links, video_links)
        except Exception as e:
            print(e)
            print('解析失败！')
            exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A Tool for downloading douyin video without watermark.')
    parser.add_argument('link', help='parse a link to download', type=str)
    # parser.add_argument('-p', '--path', help='specify download directory', type=str)
    parser.add_argument('-v', '--video', action='store_true', help='download video')
    parser.add_argument('-c', '--cover', action='store_true', help='download cover')
    parser.add_argument('-m', '--music', action='store_true', help='download music')
    parser.add_argument('-a', '--all', action='store_true', help='download video, cover and music')
    args = parser.parse_args()
    # print(args)

    if not os.path.exists('download/'):
        os.mkdir('download/')

    if args.video or args.cover or args.music or args.all:
        v = Dyd.parse_link(args.link)
        if args.all:
            v.download_all()
        else:
            if args.video:
                v.download_video()
            if args.cover:
                v.download_cover()
            if args.music:
                v.download_music()
        print(f'文件保存在 {os.getcwd()}/download')
    else:
        print('Nothing to download')

    # v = Dyd.parse_link('https://v.douyin.com/FUfwY27/')
