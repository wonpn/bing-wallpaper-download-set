var fs = require('fs');
var request = require('request');
var path = require('path');
var child = require('child_process');

var url = 'http://cn.bing.com/';

console.log("主进程开始");

request(url, function (error, response, body) {
	console.log("request进程开始");
  if (!error && response.statusCode == 200) {
    //console.log(body);    //返回请求页面的HTML
	var begin = body.indexOf("g_img={url: ")+13;
	var end = body.indexOf(",id:'bgDiv'")-1;
	
	var imgurl = body.substring(begin,end).replace(/\\/g,"");//截取url字符串，删除url中的"\"
	var filename = path.basename(imgurl);	//获取文件名
	console.log("request进程运行中");
	fs.exists("D:\\wallpaper\\" + filename, function(result) { 
	console.log("exist进程开始");
	if (result){
		console.log("壁纸已经下载！");
		return;
	}
	else{
		request(imgurl).pipe(fs.createWriteStream("D:\\wallpaper\\" + filename));  //下载文件
		console.log("下载完成！");
		
		fs.writeFileSync('path.txt', "D:\\wallpaper\\" + filename);   //写入path。txt文件路径,调用vbs设置壁纸
		console.log("写入成功！");
		
		child.exec('set.vbs', function(error, stdout, stderr){ 
			console.log("child进程开始");
			if (!error ) {
				console.log("设置壁纸成功！");
			}
			console.log("child进程结束");
		});

		//
	
	}
	console.log("exist进程结束");
	});
	
	
	
  }
	console.log("request进程结束");
});
console.log("主进程结束");
