import win32gui,win32con,win32api
import urllib.request
import os
import io
import sys
import time
import json
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #控制台中文乱码解决方案

def responsehtml(url):
	req = urllib.request.Request(url=url)
	try:
		return urllib.request.urlopen(req).read()
	except urllib.request.HTTPError as e:
		print (e.code)

def downloadjpg(imgurl):
	jpgpathname = 'D:\\wallpaper\\'+time.strftime("%Y-%m-%d", time.localtime())+".jpg"
	if os.path.isfile(jpgpathname):
		print ("已经存在壁纸："+jpgpathname)
		return jpgpathname
	else:
		jpgurl = imgurl
		if jpgurl[0] == "/":
			jpgurl = "https://www.bing.com"+jpgurl
		urllib.request.urlretrieve(jpgurl, jpgpathname)
		print ("下载壁纸完成。")
		return jpgpathname

def setWallpaper(imagepath):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "0") #2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath, 1+2)
    print ("设置为桌面壁纸成功")


url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=2'
#print(responsehtml(url))

str1 = json.loads(str(responsehtml(url), encoding = "utf-8"))
#print(str1['images'][0])
imgurl = str1['images'][0]['url']
imagepath = downloadjpg(imgurl)
setWallpaper(imagepath)
