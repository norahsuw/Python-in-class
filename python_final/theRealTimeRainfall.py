from tkinter import *
import pandas as pd    
import requests, json
def printSelection():
    global citylist,report
    report.delete("1.0","end")
    url=urllist[var.get()]
    try:
        response = requests.get(url)
        data = json.loads(response.text);
    except:
        data = None
    report.insert(INSERT,"\n")
    report.insert(INSERT,"               "+citylist[var.get()]+"目前雨量報吿\n\n")
    report.insert (INSERT,"="*44+"\n\n")
    w=data["records"]
    w2=w["location"]
    w3=w2[0]["weatherElement"]
    report.insert (INSERT,"今日降雨量："+str(w3[7]["elementValue"])+"\n")
    report.insert (INSERT,"12小時內累積雨量："+str(w3[5]["elementValue"])+"\n")
    report.insert (INSERT,"24小時內累積雨量："+str(w3[6]["elementValue"])+"\n")
    report.insert (INSERT,"兩日內累積雨量："+str(w3[8]["elementValue"])+"\n")
    report.insert (INSERT,"三日內累積雨量："+str(w3[9]["elementValue"])+"\n\n")
    report.insert (INSERT,"="*44+"\n\n")
    report.insert (INSERT,"備註,雨量小於0代表因故無資料")   

url_head ="https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0002-001?Authorization=CWB-2AAB223B-E57A-4678-96AB-848CF78CC6BC&format=JSON"
url_tail="&elementName=&parameterName=CITY"
url_0=url_head +"&locationName=%E8%87%BA%E5%8C%97" + url_tail
url_1=url_head +"&locationName=%E6%A1%83%E5%9C%92" + url_tail
url_2=url_head +"&locationName=%E6%96%B0%E7%AB%B9" + url_tail
url_3=url_head +"&locationName=%E8%8B%97%E6%A0%97" + url_tail
url_4=url_head +"&locationName=%E5%8D%97%E6%8A%95" + url_tail
url_5=url_head +"&locationName=%E8%87%BA%E4%B8%AD" + url_tail
url_6=url_head +"&locationName=%E9%AB%98%E9%90%B5%E5%BD%B0%E5%8C%96" + url_tail
url_7=url_head +"&locationName=%E9%AB%98%E9%90%B5%E9%9B%B2%E6%9E%97" + url_tail
url_8=url_head +"&locationName=%E5%98%89%E7%BE%A9" + url_tail
url_9=url_head +"&locationName=%E8%87%BA%E5%8D%97"+ url_tail
url_10=url_head +"&locationName=%E9%AB%98%E9%9B%84"+ url_tail
url_11=url_head +"&locationName=%E5%B1%8F%E6%9D%B1" + url_tail
url_12=url_head +"&locationName=%E5%AE%9C%E8%98%AD" + url_tail
url_13=url_head +"&locationName=%E8%8A%B1%E8%93%AE" + url_tail
url_14=url_head +"&locationName=%E8%87%BA%E6%9D%B1" + url_tail
win=Tk()
win.geometry("1000x700")
win.title("城市即時雨量資訊")
win.configure(bg="white")
bg = PhotoImage(file = "rain.png")
label1 = Label( win, image = bg)
label1.place(x = 100, y = 0)
label2=Label(win, text="城市即時雨量資訊",pady=6, fg="white",font=("微軟正黑體",32),bg="#88A2B9")
label2.place(x=320,y=20)
var=IntVar()
var.set(0)
citylist = {0:"台北",1:"桃園",2:"新竹",3:"苗栗",4:"南投",5:"台中",6:"彰化",7:"雲林",8:"嘉義",9:"台南",10:"高雄",11:"屏東",12:"宜蘭",13:"花蓮",14:"台東"}
urllist = {0:url_0,1:url_1,2:url_2,3:url_3,4:url_4,5:url_5,6:url_6,7:url_7,8:url_8,9:url_9,10:url_10,11:url_11,12:url_12,13:url_13,14:url_14}

for j in range(0,15):
    n = j
    if(n < len(citylist)):
        city1 = citylist[n]
        rbtem = Radiobutton(win, text=city1, variable=var, value=n, command=printSelection,bg="white")
        rbtem.place(x=20, y=j*40+45)
        if(n==0):
            rbtem.select()
report=Text(win,height=20,width=45)
report.place(x=330,y=250)
win.mainloop()
