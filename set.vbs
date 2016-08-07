'vbs文件编码为ANBI，否则中文识别有问题

WScript.Sleep 1000
If IsExitAFile(".\path.txt") Then

set fs=createobject("scripting.filesystemobject")
set ts=fs.opentextfile(".\path.txt",1,true)
bingPic=ts.readall
call setWallpaper(bingPic)


Else msgbox "图片不存在哦-_-"
End If

Function IsExitAFile(filespec)
        Dim fso
        Set fso=CreateObject("Scripting.FileSystemObject")        
        If fso.fileExists(filespec) Then         
        IsExitAFile=True        
        Else IsExitAFile=False        
        End If
End Function 


Sub setWallpaper(PicPath)
    Dim shApp, picFile, items
    Set shApp = CreateObject("Shell.Application")
    Set picFile = CreateObject("Scripting.FileSystemObject").GetFile(PicPath)
    Set items = shApp.NameSpace(picFile.ParentFolder.Path).ParseName(picFile.Name).Verbs
    For Each item In items
      If item.Name = "设置为桌面背景(&B)" Then item.DoIt
    Next
    WScript.Sleep 1000
End Sub

