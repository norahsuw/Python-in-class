from tkinter import *
import pandas as pd
import requests, json

def printSelection():
    global citylist,report
    report.delete("1.0","end")
    url=urllist[var.get()]
    try:
        response=requests.get(url)
        data=json.loads(response.text);
    except:
        data=None
    report.insert(INSERT,"           "+citylist[var.get()]+" 目前氣候報告\n")
    report.insert(INSERT,"-"*40+"\n")
    weather= data["weather"][0]
    report.insert(INSERT,"天氣描述: "+weather["description"]+"\n")
    report.insert(INSERT,"-"*40+"\n")
    main=data["main"]
    report.insert(INSERT,"目前溫度: "+str(main["temp"])+"\n")
    report.insert(INSERT,"大氣壓力: "+str(main["pressure"])+"\n")
    report.insert(INSERT,"目前濕度: "+str(main["humidity"])+"\n")
    report.insert(INSERT,"最低溫度: "+str(main["temp_min"])+"\n")
    report.insert(INSERT,"最高溫度: "+str(main["temp_max"])+"\n")
    report.insert(INSERT,"-"*40)
    
API_key="49c033d305bae8e4fce740d6d2f0e448"
country="TW"
url_head = "https://api.openweathermap.org/data/2.5/weather?"
url_tail="," + country + "&units=metric&lang=zh_tw&" + "appid=" + API_key
url_taipei=url_head  +"q=" + "Taipei" + url_tail
url_banqiao=url_head +"q="+"Banqiao" + url_tail
url_taoyuan=url_head +"q="+"Taoyuan" + url_tail
url_hsinchu=url_head +"q="+"Hsinchu" + url_tail
url_taichung=url_head +"q="+"Taichung" + url_tail
url_tainan=url_head  +"q="+"Tainan" + url_tail
url_kaohsiung=url_head +"q=" + "Kaohsiung" + url_tail

win=Tk()
win.geometry("800x500")
win.title("城市即時天氣資訊")
label1=Label(win,text="城市即時天氣資訊",pady=6,fg="darkblue",bg="lightblue",font=("微軟正黑體",16))
label1.place(x=300, y=10)
var=IntVar()
var.set(0)
citylist={0:"台北",1:"板橋",2:"桃園",3:"新竹",4:"台中",5:"台南",6:"高雄"}
urllist = {0:url_taipei, 1:url_banqiao,2:url_taoyuan ,3:url_hsinchu, 4:url_taichung, 5:url_tainan, 6:url_kaohsiung}
for i in range(0,2):
    for j in range(0,4):
        n = i* 4+j 
        if(n <len(citylist)):
            city1 = citylist[n]
            rbtem = Radiobutton(win, text=city1, variable=var, value=n,command=printSelection)
            rbtem.place(x=j*150+150,y=i*60+60)
            if(n==0): 
                rbtem.select()
report=Text(win,height=15,width=40)
report.place(x=200,y=200)
win.mainloop()