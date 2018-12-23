#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from ..models import Plant, Vegetable, Compost
from ..post_data import parse_keys, Plant_keys,parse_keys2, parse_keys3, parse_keys4
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
from datetime import datetime, timedelta
import time
import requests
import pytz
import numpy as np
from threading import Timer

def print_time():
    print "From print_time", time.time()
    
def print_some_times():
    print(time.time())
    Timer(20, print_time, ()).start()
    # Timer(, print_time, ()).start()
    # print(time.time())

tz = pytz.timezone('Asia/Bangkok')
list_nodes = ['X', 'A', 'B', 'C']

def unixtime_to_readable(unixtime):
    tz = pytz.timezone('Asia/Bangkok')
    now1 = datetime.fromtimestamp(unixtime, tz)
    month_name = now1.month
    thai_year = now1.year + 543
    time_str = now1.strftime('%H:%M:%S')
    return ("%d/%s/%d %s"%(now1.day, month_name, thai_year, time_str))

key = {
  "type": "service_account",
  "project_id": "smart-farm-27e2b",
  "private_key_id": "baf1a2bdfb82f3dda04540034ac097fa7d1d6863",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCjYNrU7AmcAvdf\n7K5zGE6dNmxJzdC/9Hh4ihy6cxDsfpkp4rNCU7K06q2gPrM6ch6aJKTPwvASrckC\ncQuymQtgytr4MFWfjjOR16PuJxxJEzNcF/OovVnDJhQhyL8z4wVX3Qwb+21Q1yyg\nuqlUQdcOfp5/DXBrw0V8yIMNRcdZlnLrsL3oxH5edbtqdzUBP/wglk7LtexSowS4\nDg6mZ2btruAXPzGqxFcyKZNrmjgKah+JgPapO9oEwef/A4dCGKNZb30ETEhONCwF\nlkET6lrmXs4Zng/dbSdTLh2X1NObov9fdKP72TtBjCvMDbqtZ17wtVeU+Grcnd6u\nqd0aczwLAgMBAAECggEAIIuHrAiE9YYFvx8HtTevWVPhCGauYb6STPi+Nkn7ohCp\n9BULvnerzqw9AAHddBQNkokgJ57eceoac5kPSnmAMbzXF7+RHuKV1USOjD9QPCJO\nBddjm0Z03hH0yrIRnIVpqBIJen2ATi0+35mvZ3BiJaoFaqvDrEPO0Meki31N88NZ\n6WGEClPp/u12mc4b0rh9LbfBhBEDHEjqWYkZOsj4fZ2e1boCHwL59yICBmsSCLS5\ngm7RBFDH8mM0ivJnwvR2ckXnUzJAsfkvM5IZ+b4062AL+1Gvjpg67GRrw7j57EBs\nP9nEakrh2Z/FfcIhQSMvBD67T4TMiBpT9aXR728vkQKBgQDZcYP/eLJHlrTdZqb6\nJkrVrpBoYy22Vq70lnIoO/cDQmScmyXc0RXJkGUFnqA9Cqti7GHXtqtdHhb1dXMM\n/O3jkQYSDtfPStL9cukoqGvwPYPH4DKDoGTGp+zV4UoptJNA/UHb8O0l/8C/fAin\nmBf4zI0DgOKBwsY/eaFMKKoLuQKBgQDAWSTuXbe66UG6wIUTF0UUcKHPMcC4tsBh\nRBLLzuTN+r629Rd4tyXbYX0nN0HcBUeWDwaeuCv3GmnxnNxpJOe8dFb0JNHfyAZF\nAsbe97JyZNTXIpTtC1PD8FoBIt5nDMN0GRgqlBVvtHo89xlPprl2gbL0ooaVuVPs\noBXPiFMP4wKBgQC3XLtD1qL4LYUtYqASN/JJSSBrdp8YsPZuOOPhO9fr/rPbQBXo\npMRrqgEWgRJ9Bx9Jly5W+qp9Jp+Ts8wmOq/cg/ILjkq8ekt8AMfPSl9jQmx7Q3s1\ndi8lOnxES+v/SVAXsLk14HAK6CXBE7Y0pdQpMU0ElE3twLLu2gGDuJLUuQKBgQC6\nYOafLiJMs56kJc4MfJzMPIMdsDjtAvAQj5Si9bvRNyk7QOvYZacCF0ndCPcBCgCe\nj7q7avv2+Ro1KuiL3V3KxvRGp7LRYxFoJ1OqU1sO61Mtju29bx9gmfGsbiwQsFZn\nlbVL9Kd80OUtU8Wr34KQKQbNcvpz89s1Sr03lgHePwKBgQC6lF7TNn6/p4l09U+d\n+2kbac7ehrjSGmSEyu75BMU8IKuoOPcEPLVj3p9vPl1lEluXyxl5tbLgI73OWC4M\nnCoEPpXoXxBGup9L7iUfspP7Jot/V9+5IGbzf40GgD8+QQpyg0TQmFcVJML13HFN\nPvJ9mGpA8G8+KJrZOQwZpAyqwA==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-atbs7@smart-farm-27e2b.iam.gserviceaccount.com",
  "client_id": "104462862666054572082",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-atbs7%40smart-farm-27e2b.iam.gserviceaccount.com"
}

cred = credentials.Certificate(key)
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://smart-farm-27e2b.firebaseio.com/'
})

    
def index(request):
    print_some_times()
    data_dict = {}
    for t in list_nodes:
        ref = db.reference(t)
        result = ref.order_by_child('time').limit_to_last(1).get()
        t = t.lower()
        for key, val in result.items():
            data_dict["{}_air_humidity".format(t)] = val["data"]["air_humidity"]
            data_dict["{}_air_temperature".format(t)] = val["data"]["air_temperature"]
            data_dict["{}_soil_temperature".format(t)] = val["data"]["soil_temperature"]
            data_dict["{}_soil_moisure".format(t)] = val["data"]["soil_moisure"]
            data_dict["updated_date_{}".format(t)] = unixtime_to_readable(val["time"] )
            
    _v = Vegetable.objects.all()
    _p = Plant.objects.filter(is_harvested=False)
    p_data = []
    for i in _p:
        di = {}
        di["start_plant_timestamp"] = i.start_plant_timestamp.strftime("%d/%m/%Y")
        year = int(i.start_plant_timestamp.strftime("%Y"))-543
        day = i.start_plant_timestamp.strftime("%d")
        month = i.start_plant_timestamp.strftime("%m")
        time = str(day)+"/"+str(month)+"/"+str(year)
        date_time_obj = datetime.strptime(time, '%d/%m/%Y')
        dif_time = (datetime.now() - date_time_obj)
        if(int(dif_time.days) <=  0):
            d = 0
        else:
            d = dif_time.days
        di["plant_type"] = i.plant_type
        di["sensor"] = i.sensor
        di["id"] = i.id
        di["duration"] = d
        p_data.append(di)
    
    refStatus = db.reference('Valve_Status')
    valve1 = str(refStatus.child('Valve1').get())
    valve2 = str(refStatus.child('Valve2').get())
    if valve1 == "off":
        state1 = "false"
        _b1 = ""
    else:
        state1 = "true"
        _b1 = "active"
    if valve2 == "off":
        state2 = "false"
        _b2 = ""
    else:
        state2 = "true"
        _b2 = "active"
        
    return_dict = {
        "vegs": _v,
        "plant": p_data,
        "state1": state1,
        "button1": _b1,
        "state2": state2,
        "button2": _b2
    }
    return_dict.update(data_dict)
    
    return render(request, "index.html", return_dict)

def control(request):
    
    data_dict = {}
    for t in list_nodes:
        ref = db.reference(t)
        result = ref.order_by_child('time').limit_to_last(1).get()
        t = t.lower()
        for key, val in result.items():
            data_dict["{}_air_humidity".format(t)] = val["data"]["air_humidity"]
            data_dict["{}_air_temperature".format(t)] = val["data"]["air_temperature"]
            data_dict["{}_soil_temperature".format(t)] = val["data"]["soil_temperature"]
            data_dict["{}_soil_moisure".format(t)] = val["data"]["soil_moisure"]
            data_dict["{}_time".format(t)] = unixtime_to_readable(val["time"])
    return render(request, "control.html", data_dict)
    

def history(request):
    _p = Plant.objects.filter(is_harvested=True)
    _v = Vegetable.objects.all()
    data = []
    for i in _p:
        data.append(i.plant_type)
    data = set(data)
        
    return render(request,"history.html", {"plant":_p, "vegs":_v, "dataset":data})
    
def view_history(request):
    p_t = request.POST.get("p_t")
    if(p_t == "all"):
        _p = Plant.objects.all()
    else:
        _p = Plant.objects.filter(is_harvested=True, plant_type=p_t)
    p_data = []
    node_val = []
    for i in _p:
        di = {}
        di["start_date"] = i.start_plant_timestamp.strftime("%d/%m/%Y")
        di["end_date"] = i.end_plant_timestamp.strftime("%d/%m/%Y")
        di["plant_type"] = i.plant_type
        di["sensor"] = i.sensor
        di["id"] = i.id
        di["totals"] = str(i.keep_total)+" "+i.keep_unit
        if( i.sensor == u'ตู้ต้นแปลง' ):
            node = "C"
        elif(i.sensor == u'ตู้กลางแปลง'):
            node = "B"
        else:
            node = "A"
        value = get_value_from_date(di["start_date"], di["end_date"], node, di["id"])
        node_val.append(value)
        p_data.append(di)
    _c = Compost.objects.all()
    c_data = []
    i=1
    for v in _c:
        di = {}
        di["id"] = v.pk
        di["p_id"] = v.plant_id
        di["number"] = i
        di["date"] = v.compost_date.strftime("%d/%m/%Y")
        di["type"] = v.compost_type
        di["totals"] = str(v.compost_total) + " " + v.compost_unit
        di["total"] = v.compost_total
        di["unit"] = v.compost_unit
        c_data.append(di)
        i= i+1
    
    return render(request,"view_history.html", {"p_t":p_t ,"plant":p_data, "compost":json.dumps(c_data), "history":json.dumps(p_data), "node_val":json.dumps(node_val)})
    
def del_history(request):
    v_id = request.POST.get("p_t")
    ids = json.loads(request.POST.get("delete-ids"))
    Plant.objects.filter(pk__in=ids).delete()
    return redirect("/history/")
    
def valve(request):
    refA = db.reference('Valve_Status')
    valve1 = str(refA.child('Valve1').get())
    valve2 = str(refA.child('Valve2').get())
    if valve1 == "off":
        state1 = "false"
        _b1 = ""
    else:
        state1 = "true"
        _b1 = "active"
    if valve2 == "off":
        state2 = "false"
        _b2 = ""
    else:
        state2 = "true"
        _b2 = "active"
    return render(request, "valve.html", {
        "state1": state1,
        "button1": _b1,
        "state2": state2,
        "button2": _b2,
    })
    
def valve_state(request):
    valve = db.reference('Valve_Status')
    
    v = int(request.GET.get('valve'))
    s = str(request.GET.get('status'))
    if v == 1:
        if s == "on":
            print("on1")
            
            valve.update({
                'Valve1': 'on'
            })
        elif s == "off": 
            print("off1")
            valve.update({
                'Valve1': 'off'
            })
            
    elif v == 2:
        if s == "on":
            print("on2")
            valve.update({
                'Valve2': 'on'
            })
        elif s == "off": 
            print("off2")
            valve.update({
                'Valve2': 'off'
            })
    return HttpResponse("")
    
def graph(request):
    refX = db.reference('X')
    result_x = refX.order_by_child('time').limit_to_last(80).get()
    x_array_json_air_humid = []
    x_array_json_air_temp = []
    x_array_json_soil_moisure = []
    x_array_json_soil_temp = []
    for key, val in result_x.items():
        x_json_air_humid = {'x' : val["time"]*1000,
                            'y' : val["data"]["air_humidity"]
                            }
        x_json_air_temp = {'x' : val["time"]*1000,
                            'y' : val["data"]["air_temperature"]
                            }
        x_json_soil_moisure = {'x' : val["time"]*1000,
                            'y' : val["data"]["soil_moisure"]
                            }
        x_json_soil_temp = {'x' : val["time"]*1000,
                            'y' : val["data"]["soil_temperature"]
                            }
        x_array_json_air_humid.append(x_json_air_humid)
        x_array_json_air_temp.append(x_json_air_temp)
        x_array_json_soil_moisure.append(x_json_soil_moisure)
        x_array_json_soil_temp.append(x_json_soil_temp)
        
    refA = db.reference('A')
    result_a = refA.order_by_child('time').limit_to_last(80).get()
    a_array_json_air_humid = []
    a_array_json_air_temp = []
    a_array_json_soil_moisure = []
    a_array_json_soil_temp = []
    for key, val in result_a.items():
        a_json_air_humid = {'x' : val["time"]*1000,
                            'y' : val["data"]["air_humidity"]
                            }
        a_json_air_temp = {'x' : val["time"]*1000,
                            'y' : val["data"]["air_temperature"]
                            }
        a_json_soil_moisure = {'x' : val["time"]*1000,
                            'y' : val["data"]["soil_moisure"]
                            }
        a_json_soil_temp = {'x' : val["time"]*1000,
                            'y' : val["data"]["soil_temperature"]
                            }
        a_array_json_air_humid.append(a_json_air_humid)
        a_array_json_air_temp.append(a_json_air_temp)
        a_array_json_soil_moisure.append(a_json_soil_moisure)
        a_array_json_soil_temp.append(a_json_soil_temp)
    
    refB = db.reference('B')
    result_b = refB.order_by_child('time').limit_to_last(80).get()
    b_array_json_air_humid = []
    b_array_json_air_temp = []
    b_array_json_soil_moisure = []
    b_array_json_soil_temp = []
    for key, val in result_b.items():
        b_json_air_humid = {'x' : val["time"]*1000,
                            'y' : val["data"]["air_humidity"]
                            }
        b_json_air_temp = {'x' : val["time"]*1000,
                            'y' : val["data"]["air_temperature"]
                            }
        b_json_soil_moisure = {'x' : val["time"]*1000,
                            'y' : val["data"]["soil_moisure"]
                            }
        b_json_soil_temp = {'x' : val["time"]*1000,
                            'y' : val["data"]["soil_temperature"]
                            }
        b_array_json_air_humid.append(b_json_air_humid)
        b_array_json_air_temp.append(b_json_air_temp)
        b_array_json_soil_moisure.append(b_json_soil_moisure)
        b_array_json_soil_temp.append(b_json_soil_temp)
    
    refC = db.reference('C')
    result_c = refC.order_by_child('time').limit_to_last(80).get()
    c_array_json_air_humid = []
    c_array_json_air_temp = []
    c_array_json_soil_moisure = []
    c_array_json_soil_temp = []
    for key, val in result_c.items():
        c_json_air_humid = {'x' : val["time"]*1000,
                            'y' : val["data"]["air_humidity"]
                            }
        c_json_air_temp = {'x' : val["time"]*1000,
                            'y' : val["data"]["air_temperature"]
                            }
        c_json_soil_moisure = {'x' : val["time"]*1000,
                            'y' : val["data"]["soil_moisure"]
                            }
        c_json_soil_temp = {'x' : val["time"]*1000,
                            'y' : val["data"]["soil_temperature"]
                            }
        c_array_json_air_humid.append(c_json_air_humid)
        c_array_json_air_temp.append(c_json_air_temp)
        c_array_json_soil_moisure.append(c_json_soil_moisure)
        c_array_json_soil_temp.append(c_json_soil_temp)
    
    return render(request, "graph.html", {"x_air_humidity": json.dumps(x_array_json_air_humid),
                                          "x_air_temperature": json.dumps(x_array_json_air_temp),
                                          "x_soil_moisure": json.dumps(x_array_json_soil_moisure),
                                          "x_soil_temperature": json.dumps(x_array_json_soil_temp),
                                      
                                          "a_air_humidity": json.dumps(a_array_json_air_humid),
                                          "a_air_temperature": json.dumps(a_array_json_air_temp),
                                          "a_soil_moisure": json.dumps(a_array_json_soil_moisure),
                                          "a_soil_temperature": json.dumps(a_array_json_soil_temp),
                                      
                                          "b_air_humidity": json.dumps(b_array_json_air_humid),
                                          "b_air_temperature": json.dumps(b_array_json_air_temp),
                                          "b_soil_moisure": json.dumps(b_array_json_soil_moisure),
                                          "b_soil_temperature": json.dumps(b_array_json_soil_temp),
                                      
                                          "c_air_humidity": json.dumps(c_array_json_air_humid),
                                          "c_air_temperature": json.dumps(c_array_json_air_temp),
                                          "c_soil_moisure": json.dumps(c_array_json_soil_moisure),
                                          "c_soil_temperature": json.dumps(c_array_json_soil_temp),
                                          })

def get_value_from_date(start, end, node, p_id):
    
    date_start = []
    date_end = []
    date_start = start.split("/")
    date_start[2] = int(date_start[2])-543
    time = date_start[0]+"/"+date_start[1]+"/"+str(date_start[2])
    date_start_obj = datetime.strptime(time, '%d/%m/%Y')
    unix_date_start = date_start_obj.strftime("%s")
    
    date_end = end.split("/")
    date_end[2] = int(date_end[2])-543
    time = date_end[0]+"/"+date_end[1]+"/"+str(date_end[2])
    date_end_obj = datetime.strptime(time, '%d/%m/%Y')
    unix_date_end = date_end_obj.strftime("%s")

    
    ref = db.reference(node)
    result = ref.order_by_child('time').start_at(int(unix_date_start)).end_at(int(unix_date_end)).get()
    time = []
    air_humidity = []
    air_temperature = []
    soil_temperature = []
    soil_moisure = []
    for key, val in result.items():
       
        air_humidity.append(val["data"]["air_humidity"])
        air_temperature.append(val["data"]["air_temperature"])
        soil_temperature.append(val["data"]["soil_temperature"])
        soil_moisure.append(val["data"]["soil_moisure"])
    
    value = {"p_id" : p_id,
             "air_humid_avg" : round(np.mean(air_humidity),2),
             "air_humid_max" : round(np.amax(air_humidity),2),
             "air_humid_min" : round(np.amin(air_humidity),2),
             
             "air_temp_avg" : round(np.mean(air_temperature),2),
             "air_temp_max" : round(np.amax(air_temperature),2),
             "air_temp_min" : round(np.amin(air_temperature),2),
             
             "soil_moi_avg" : round(np.mean(soil_moisure),2),
             "soil_moi_max" : round(np.amax(soil_moisure),2),
             "soil_moi_min" : round(np.amin(soil_moisure),2),
             
             "soil_temp_avg" : round(np.mean(soil_temperature),2),
             "soil_temp_max" : round(np.amax(soil_temperature),2),
             "soil_temp_min" : round(np.amin(soil_temperature),2)
             }
    return value
    