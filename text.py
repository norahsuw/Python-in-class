data1=[]
data2=[]
data3=[]
with open('text1.txt','r',encoding="utf-8") as t1_obj:
    with open('text2.txt','r',encoding="utf-8") as t2_obj:
        with open('text3.txt','a',encoding="utf-8") as t3_obj:
            for line1 in t1_obj:
                data1.append(line1)
            for line2 in t2_obj:
                data2.append(line2)
            print(data1)
            print(data2)
            comb=min(len(data1),len(data2))
            for i in range(comb):
                data3.append(data1[i])
                data3.append(data2[i])
            if len(data1)>len(data2):
                for k in range(comb,len(data1)):
                    data3.append(data1[k])
            else :
                for k in range(comb,len(data2)):
                    data3.append(data2[k])
            for j in range(len(data1)+len(data2)):
                t3_obj.write(str(data3[j]))