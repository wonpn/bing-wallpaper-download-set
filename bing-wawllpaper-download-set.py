
import urllib.request
import time
import os
import win32gui,win32con,win32api

def responsehtml(url):
	req = urllib.request.Request(url=url)
	try:
		return urllib.request.urlopen(req).read()
	except urllib.request.HTTPError as e:
		print (e.code)

def downloadjpg(html):
	jpgurlbegin = html.find("g_img={url: ")
	jpgpathname = 'D:\\wallpaper\\'+time.strftime("%Y-%m-%d", time.localtime())+".jpg"
	if jpgurlbegin == -1:
		print ("匹配壁纸路径失败！")
		return
	elif os.path.isfile(jpgpathname):
		print ("已经存在壁纸："+jpgpathname)
		return jpgpathname
	else:
		jpgurl = html[int(jpgurlbegin)+13:int(jpgurlbegin)+89]
		urllib.request.urlretrieve(jpgurl, jpgpathname)
		print ("下载壁纸完成。")
		return jpgpathname

def setWallpaper(imagepath):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "0") #2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,imagepath, 1+2)
    print ("设置为桌面壁纸成功")

url = 'http://cn.bing.com/?mkt=zh-CN'
html = str(responsehtml(url))
imagepath = downloadjpg(html)
setWallpaper(imagepath)