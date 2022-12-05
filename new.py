import json
import os

def parseJson(jsonFile):
    objs = []
    obj = []
    info = jsonFile
    name = ""
    name = info['name']
    temp1 = int(len(info))
    if temp1<2:
        return name, obj
    # print("个数:"+str(temp1))
    objects = info['labels']
    temp=0
    list_x = []
    list_y = []
    for i in objects:
        if i['category']=="crosswalk":
            length = len(i["poly2d"][0]['vertices'])
            for j in range(length):
                list_x.append(int(i["poly2d"][0]['vertices'][j][0]))
                list_y.append(int(i["poly2d"][0]['vertices'][j][1]))



    if list_x:
        # print(name)
        x1 = min(list_x)
        x2 = max(list_x)
        y1 = min(list_y)
        y2 = max(list_y)
        # print(str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2))
        obj.append(x1)
        obj.append(y1)
        obj.append(x2)
        obj.append(y2)
        obj.append(0)
    return name, obj


def change(x1, y1, x2, y2):
    w=1280
    h=720
    x_ = (x1 + x2) / (2*w)
    y_ = (y1 + y2) / (2*h)
    w_ = (x2 - x1) / w
    h_ = (y2 - y1) / h

    return x_, y_, w_, h_

file_handle = open('lane_train.txt', mode='a')
f = open("lane_train.json")
info = json.load(f)
objects = info
n = len(objects)#样本个数 train70000 val10000
count = 0
for i in range(n):
    an = ""
    name, result= parseJson(objects[i])
    if result:
        temp_path = "./train/"+name[:18]+'txt'
        print(temp_path)
        file_txt = open(temp_path, mode='x')
        (x_), y_, w_, h_ = change(result[0], result[1], result[2], result[3])
        content = '0 ' + str(x_) + ' ' + str(y_) + ' ' + str(w_) + ' ' + str(h_)
        file_txt.write(content)
        file_txt.close()

        an = '\n' + "./bdd100k/images/100k/train" + name
        an = an + ' ' + str(result[0]) + ',' + str(result[1]) + ',' + str(result[2]) + ',' + str(
                result[3]) + ',' + str(0)
        # an = an + '\n'
        count += 1
    file_handle.write(an)
    # print(count)

