# douyin-dl 国人都在用的抖音视频下载器
![Python](https://img.shields.io/badge/Python-3.10-blue)

## 序言

相信有不少人在使用抖音时都有下载视频的需求，但是从官方APP下载的视频会有原作者的水印。这无疑让我们这种强迫症患者非常难受。

因此，本工具诞生了！它不仅能够下载无水印的视频，而且支持同时下载视频的音乐和封面，简直是太好用啦！比那些在线解析的小网站不知高到哪里去。

## 声明

**本工具仅为短视频创作者、视频收藏者等人提供便捷，因此不支持批量下载视频！**

## 如何使用

### 下载工具

```bash
git clone https://github.com/hadwinfu/douyin-dl.git
```

### 安装依赖

```bash
cd douyin-dl
pip install -r requirements.txt
```

### 赋予执行权限

```bash
chmod +x dyd.py
```

### 使用方法

```bash
usage: dyd.py [-h] [-v] [-c] [-m] [-a] link

A Tool for downloading douyin video without watermark.

positional arguments:
  link         parse a link to download

options:
  -h, --help   show this help message and exit
  -v, --video  download video
  -c, --cover  download cover
  -m, --music  download music
  -a, --all    download video, cover and music
```

默认下载至程序所在目录，暂不支持指定存放路径。

### 栗子

当你复制了分享链接

只下载视频

```bash
python dyd.py https://v.douyin.com/FUfwY27/ -v

或者

./dyd.py https://v.douyin.com/FUfwY27/ -v
```

只下载音乐

```bash
./dyd.py https://v.douyin.com/FUfwY27/ -m
```

下载视频和封面

```bash
./dyd.py https://v.douyin.com/FUfwY27/ -v -c
```

下载所有（视频、封面、音乐）

```bash
./dyd.py https://v.douyin.com/FUfwY27/ -a
```

**没错！一切都是那么优雅！**

![douyin-dl.png](https://s2.loli.net/2022/05/10/U8MGcg75IFTet1k.png)

## 致谢

感谢我自己。