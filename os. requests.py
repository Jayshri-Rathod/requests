import requests
import json

url=requests.get("http://saral.navgurukul.org/api/courses")
data=url.json()
with open("course.json","w")as file:
    json.dump(data,file,indent=4)
serial=1
name_list=[]
for i in data["availableCourses"]:
    print(serial,i["name"],i["id"])
    name_list.append(i["name"])
    serial+=1
topic_name=int(input("enter serial id:-"))
serial=topic_name
print(" ",name_list[serial-1])
url2=requests.get("http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][topic_name-1]["id"])+"/exercises")
data2=url2.json()
with open("course_parent.json","w")as file2:
    json.dump(data2,file2,indent=4)

serial2=1
child_list=[]
for j in data2["data"]:
    print("      ",serial2,j["name"])
    child_list.append(j["name"])
    serial2+=1
child_name=(int(input('enter child serial number:-')))
serial2=child_name
a=child_list[serial2-1]
print("   ",a)
s=1
ques_list=[]
slug_list=[]
for i in data2["data"]:
    if i["name"]==a:
        if len(i["childExercises"])==0:
            slug_list.append(i["slug"])
            print("       ",s,i["slug"])
            s+=1
        else:
            for que in i["childExercises"]:
                ques_list.append(que["name"])
                print("        ",s,que["name"])
                s+=1
child_no=int(input("enter child number:-"))
for i in range(len(ques_list)):
    url3=requests.get("http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][topic_name-1]["id"])+"/exercise/getBySlug?slug="+str(data2["data"][child_name-1]["childExercises"][child_no-1]["slug"]))
    DATA=url3.json()
    with open("ques.json","w") as f:
        json.dump(DATA,f,indent=4)
        print(DATA["content"])
        break
else:
    for i in range(len(slug_list)):
        url3=requests.get("http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][topic_name-1]["id"])+"/exercise/getBySlug?slug="+str(data2["data"][child_no-1]["slug"]))
        d=url3.json()
        with open("ques1.json","w") as f:
            json.dump(d,f,indent=4)
            print(d["content"])
            break
        

