import requests
import json

x = requests.get("http://join.navgurukul.org/api/partners")
Data = x.json()

with open("data1.json","w") as f:
    json.dump(Data,f,indent=4)

serial=1
name_list=[]
id_list=[]
for index in Data["data"]:
    print(serial,"-",index["name"],index["id"])
    name_list.append(index["name"])
    id_list.append(index["id"])
    serial+=1

dict={}
for i in range(len(name_list)):
    dict.update({name_list[i]:id_list[i]})
print("  ")

y=input("enter what do you want to do asending(a) or desending(d):-")
print("  ")
if y=="a":

    list_value=[]
    for i in dict:
        a=dict[i]
        list_value.append(i)
        list_value.append(a)
    k=1
    while k<len(list_value):
        j=k+2
        while j<len(list_value):
            if list_value[k]>list_value[j]:
                c=list_value[k]
                list_value[k]=list_value[j]         
                list_value[j]=c
                i=a
            j+=2
        k+=2
    i=0
    s=1
    while i<len(list_value):
        print(s,"-",list_value[i],list_value[i+1])
        s+=1
        i+=2
elif y=="d":
    list_value=[]
    for i in range(len(dict)):
        max_1=0
        for value in dict:
            if max_1<dict[value]:
                max_1=dict[value]
                key=value
        list_value.append(key) 
        list_value.append(max_1)
        dict.pop(key)
    # print(list_value)
    i=0
    s=1
    while i<len(list_value):
        print(s,"-",list_value[i],list_value[i+1])
        s+=1
        i+=2
else:
    print("Sorry! No choice")
        
