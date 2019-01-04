#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
# -*- coding: UTF-8 -*-
from tkinter.messagebox import *
import os
import tkinter

win = tkinter.Tk()
win.title("monkey")
win.geometry("600x600+300+300")
event_num = tkinter.StringVar()
for_time = tkinter.StringVar()
apk_name = tkinter.StringVar()
radVar = tkinter.StringVar()

def createPage():
    #界面
    label1 = tkinter.Label(win,text="事件数")
    entry1 = tkinter.Entry(win, textvariable = event_num)
    label2 = tkinter.Label(win,text="种子数")
    entry2 = tkinter.Entry(win, textvariable = for_time)
    Button1 = tkinter.Button(win,text="Run",width=6,bg="blue",command=Check)
    Button2 = tkinter.Button(win,text="退出",width=6,bg="red",command=win.quit)
    entry3 = tkinter.Entry(win,textvariable = apk_name)
    #列表空间
    listb = tkinter.Listbox(win,width=30,height=15)
    applist = get_package()
    for item in applist:
        listb.insert(0, item)
    def getContent():
        lists = listb.get(listb.curselection())
        apk_name.set(lists.split(":")[-1])
    Button3 = tkinter.Button(win, text='确认', bg='blue', command= getContent, width=6)
    #选择控件（单选）
    label4 = tkinter.Label(win, text="请选择日志级别：")
    Level1 = "一级"
    Level2 = "二级"
    Level3 = "三级"
    radVar.set("-v -v -v")
    rad1 = tkinter.Radiobutton(win, text=Level1, variable=radVar, value="-v")
    rad2 = tkinter.Radiobutton(win, text=Level2, variable=radVar, value="-v -v")
    rad3 = tkinter.Radiobutton(win, text=Level3, variable=radVar, value="-v -v -v")
    #空间布局
    rad1.place(x=300, y=130)
    rad2.place(x=370, y=130)
    rad3.place(x=440, y=130)
    label1.place(x=300,y=0)
    entry1.place(x=350,y=0)
    label2.place(x=300,y=50)
    entry2.place(x=350,y=50)
    Button1.place(x=10,y=400)
    Button2.place(x=400,y=400)
    listb.place(x=10,y=0)
    entry3.place(x=90, y=270)
    Button3.place(x=10, y=270)
    label4.place(x=300, y=100)
    win.mainloop()
#获取手机所有的安装包
def get_package():
    pkg = os.popen("adb shell pm list packages").readlines()
    list = []
    for line in pkg:
        list.append(line.replace("\n", ""))
    return (list)

def Check():
    event = event_num.get()
    for_times = for_time.get()
    apk = apk_name.get()
    level = radVar.get()
    #检查手机连接状态
    phonedevice = os.popen('adb devices').read()
    #判断monkey可执行条件
    if phonedevice.strip().endswith('device'):
        if event.isdigit() and int(event) > 0 and for_times.isdigit() and int(for_times) > 0 and apk:
         log_path = './monkey.txt'
         monkey_shell = 'adb shell monkey -p ' + apk + ' -s ' + for_times + ' --ignore-crashes --ignore-timeouts --monitor-native-crashes '+ level +" "+ event + ' > ' + log_path
         os.system(monkey_shell)
         showinfo(title='monkey运行成功', message="在根目录下查看日志monkey.txt")
        else:
            showinfo(title='错误', message="请按提示输入正确的信息")
    else:
        showinfo(title='错误', message="请连接手机")

if __name__ == '__main__':
    createPage()