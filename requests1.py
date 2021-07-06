import requests
import json
import os
from os import path


saral= requests.get("http://saral.navgurukul.org/api/courses")
Data = saral.json()
with open("data.json","w") as f:
    json.dump(Data,f,indent=4)
serial_number=1
list_name=[]
for index in Data["availableCourses"]:
    print(serial_number,index["name"],index["id"])
    list_name.append(index["name"])
    serial_number+=1

topic_1=int(input("Enter the topic number:"))
a=input("Enter where you want to go next or previous(n/p):")
serial_number=topic_1
print(list_name[serial_number-1])

if a=="p":
    serial_number=1
    for index in Data["availableCourses"]:
        print(serial_number,index["name"],index["id"])
        serial_number+=1
    topic_1=int(input("Enter the topic number:"))

# saral2=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic_1-1]["id"])+"/exercises")
# data=saral2.json()
# with open("parent.json","w") as f:
#     json.dump(data,f,indent=4)

# serial1=1
# serial_2=1
# topic_list=[]
# for i in data["data"]:
#     if len(i["childExercises"])==0:
#         print("     ",serial1,i["name"])
#         topic_list.append(i["name"])
#         print("        ",serial_2,i["slug"])
#         serial1+=1
#     else:
#         serial_no2=1
#         print("   ",serial1,i["name"])
#         topic_list.append(i["name"])
#         for questions in i["childExercises"]:
#             print("         ",serial_no2,questions["name"])
#             serial_no2+=1
#         serial1+=1

# a=input("Enter where you want to go next or previous(n/p):")
# if a=="p":
#     sserial1=1
#     serial_2=1
#     topic_list=[]
#     for i in data["data"]:
#         if len(i["childExercises"])==0:
#             print("     ",serial1,i["name"])
#             topic_list.append(i["name"])
#             print("        ",serial_2,i["slug"])
#             serial1+=1
#         else:
#             serial_no2=1
#             print("   ",serial1,i["name"])
#             topic_list.append(i["name"])
#             for questions in i["childExercises"]:
#                 print("         ",serial_no2,questions["name"])
#                 serial_no2+=1
#             serial1+=1

# slug=int(input("Enter the parent number:"))
# question_list=[]
# slug_list=[]
# print("     ",slug,topic_list[slug-1])

# for index1 in data["data"][slug-1]["childExercises"]:
#     s=1
#     for index1 in data["data"][slug-1]["childExercises"]:
#         print("           ",s,index1["name"])
#         question_list.append(index1["name"])
#         s+=1
#     que=int(input("Enter question number:")) 
#     w=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic_1-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que-1]["slug"]))
#     DATA=w.json()
#     with open("question.json","w") as f:
#         json.dump(DATA,f,indent=4)
#         print(DATA["content"])
#         break

# for i in range(len(question_list)):
#     a=input("Enter where you want to go next or previous(n/p):")
#     if a=="n":
#         if que==len(question_list): 
#             print("Next page.")
#             break
#         else:
#             w=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic_1-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que]["slug"]))
#             DATA=w.json()
#             with open("question.json","w") as f:
#                 json.dump(DATA,f,indent=4)
#                 print(DATA["content"])
#                 que=que+1
#                 break
#     if a=="p":
#         if que==len(question_list):
#             print("No more questions")
#             break
#         else:
#             w=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic_1-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que-2]["slug"]))
#             DATA=w.json()
#             with open("question.json","w") as f:
#                 json.dump(DATA,f,indent=4)
#                 print(DATA["content"])
#                 que=que-1
# else:
#     s_no=1
#     print("           ",s_no,".",data["data"][slug-1]["slug"])
#     slug_list.append(data["data"][slug-1]["slug"])

#     que=int(input("Enter question number:"))
#     v=requests.get("http://saral.navgurukul.org/api/courses/"+str(Data["availableCourses"][topic_1-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["slug"]))
#     d=v.json()
#     with open("questions.json","w") as f:
#         json.dump(d,f,indent=4)
#         print(d["content"])
#     for i in range(len(slug_list)):
#         a=input("Enter where you want to go next or previous:(n/p)")
#         if a=="n":
#             print("Next page.")
#             break
#         if a=="p":
#             print("No more questions.")
#             break
