from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from models import Plant, Vegetable, Compost
from post_data import parse_keys, Plant_keys,parse_keys2, parse_keys3, parse_keys4
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
from datetime import datetime, timedelta
import time
import requests

# from django.utils import timezone

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
    refX = db.reference('X')
    resultX = refX.order_by_child('time').limit_to_last(1).get()
    for key, val in resultX.items():
        x_air_humidity = val["data"]["air_humidity"]
        x_air_temperature = val["data"]["air_temperature"]
        x_soil_temperature = val["data"]["soil_temperature"]
        x_soil_moisure = val["data"]["soil_moisure"]
        
    refA = db.reference('A')
    resultA = refA.order_by_child('time').limit_to_last(1).get()
    for key, val in resultA.items():
        a_air_humidity = val["data"]["air_humidity"]
        a_air_temperature = val["data"]["air_temperature"]
        a_soil_temperature = val["data"]["soil_temperature"]
        a_soil_moisure = val["data"]["soil_moisure"]
        
    refB = db.reference('B')
    resultB = refB.order_by_child('time').limit_to_last(1).get()
    for key, val in resultB.items():
        b_air_humidity = val["data"]["air_humidity"]
        b_air_temperature = val["data"]["air_temperature"]
        b_soil_temperature = val["data"]["soil_temperature"]
        b_soil_moisure = val["data"]["soil_moisure"]
        
    refC = db.reference('C')
    resultC = refC.order_by_child('time').limit_to_last(1).get()
    for key, val in resultC.items():
        c_air_humidity = val["data"]["air_humidity"]
        c_air_temperature = val["data"]["air_temperature"]
        c_soil_temperature = val["data"]["soil_temperature"]
        c_soil_moisure = val["data"]["soil_moisure"]
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
    return render(request, "index.html", {
        "vegs": _v,
        "plant": p_data,
        "state1": state1,
        "button1": _b1,
        "state2": state2,
        "button2": _b2,
        "x_air_humidity": x_air_humidity,
        "x_air_temperature": x_air_temperature,
        "x_soil_temperature": x_soil_temperature,
        "x_soil_moisure": x_soil_moisure,
        "a_air_humidity": a_air_humidity,
        "a_air_temperature": a_air_temperature,
        "a_soil_temperature": a_soil_temperature,
        "a_soil_moisure": a_soil_moisure,
        "b_air_humidity": b_air_humidity,
        "b_air_temperature": b_air_temperature,
        "b_soil_temperature": b_soil_temperature,
        "c_soil_moisure": c_soil_moisure,
        "c_air_humidity": c_air_humidity,
        "c_air_temperature": c_air_temperature,
        "c_soil_temperature": c_soil_temperature,
        "c_soil_moisure": c_soil_moisure,
    })

def control(request):
    refX = db.reference('X')
    resultX = refX.order_by_child('time').limit_to_last(1).get()
    for key, val in resultX.items():
        x_air_humidity = val["data"]["air_humidity"]
        x_air_temperature = val["data"]["air_temperature"]
        x_soil_temperature = val["data"]["soil_temperature"]
        x_soil_moisure = val["data"]["soil_moisure"]
        
    refA = db.reference('A')
    resultA = refA.order_by_child('time').limit_to_last(1).get()
    for key, val in resultA.items():
        a_air_humidity = val["data"]["air_humidity"]
        a_air_temperature = val["data"]["air_temperature"]
        a_soil_temperature = val["data"]["soil_temperature"]
        a_soil_moisure = val["data"]["soil_moisure"]
        
    refB = db.reference('B')
    resultB = refB.order_by_child('time').limit_to_last(1).get()
    for key, val in resultB.items():
        b_air_humidity = val["data"]["air_humidity"]
        b_air_temperature = val["data"]["air_temperature"]
        b_soil_temperature = val["data"]["soil_temperature"]
        b_soil_moisure = val["data"]["soil_moisure"]
        
    refC = db.reference('C')
    resultC = refC.order_by_child('time').limit_to_last(1).get()
    for key, val in resultC.items():
        c_air_humidity = val["data"]["air_humidity"]
        c_air_temperature = val["data"]["air_temperature"]
        c_soil_temperature = val["data"]["soil_temperature"]
        c_soil_moisure = val["data"]["soil_moisure"]
    return render(request, "control.html", {"x_air_humidity": x_air_humidity,
                                            "x_air_temperature": x_air_temperature,
                                            "x_soil_temperature": x_soil_temperature,
                                            "x_soil_moisure": x_soil_moisure,
                                            "a_air_humidity": a_air_humidity,
                                            "a_air_temperature": a_air_temperature,
                                            "a_soil_temperature": a_soil_temperature,
                                            "a_soil_moisure": a_soil_moisure,
                                            "b_air_humidity": b_air_humidity,
                                            "b_air_temperature": b_air_temperature,
                                            "b_soil_temperature": b_soil_temperature,
                                            "c_soil_moisure": c_soil_moisure,
                                            "c_air_humidity": c_air_humidity,
                                            "c_air_temperature": c_air_temperature,
                                            "c_soil_temperature": c_soil_temperature,
                                            "c_soil_moisure": c_soil_moisure,})
    

def history(request):
    return render(request,"history.html")
    
def meter(request):
    refA = db.reference('A')
    result = refA.order_by_child('time').limit_to_last(1).get()
    for key, val in result.items():
        air_humidity = val["data"]["air_humidity"]
        air_temperature = val["data"]["air_temperature"]
        soil_temperature = val["data"]["soil_temperature"]
        soil_moisure = val["data"]["soil_moisure"]
    return render(request, "meter.html", {"air_humidity":air_humidity,
                                          "air_temperature": air_temperature,
                                          "soil_temperature": soil_temperature,
                                          "soil_moisure": soil_moisure})
    
def view_vegetable(request):
    _v = Vegetable.objects.all()
    return render(request, "view_vegetable.html", {"vegs": _v})
    
def view_compost(request, id):
    _c = Compost.objects.filter(plant_id=id)
    _p = Plant.objects.get(pk=id)
    c_data = []
    i=1
    for v in _c:
        di = {}
        di["id"] = v.pk
        di["number"] = i
        di["date"] = v.compost_date.strftime("%d/%m/%Y")
        di["type"] = v.compost_type
        di["totals"] = str(v.compost_total) + " " + v.compost_unit
        di["total"] = v.compost_total
        di["unit"] = v.compost_unit
        c_data.append(di)
        i= i+1
    print(c_data)
    
    return render(request, "view_compost.html", {"compost": c_data , "plant":_p ,"c_js": json.dumps(c_data)})
    
def new_vegetable(request):
    return render(request, "new_vegetable.html")

def add_vegetable(request):
    if request.method == "POST":
        parsed_val = parse_keys(Plant_keys, request.POST)
        _v = Vegetable(**parsed_val)
        _v.save()
    return redirect("/vegetables/view/")
    
def add_plant(request):
    if request.method == "POST":
        time = str(request.POST.get("start-plant-timestamp")) 
        date_time_obj = datetime.strptime(time, '%d/%m/%Y')
        parsed_val = parse_keys2(request.POST.get("plant-type"), date_time_obj, request.POST.get("sensor"))
        _p = Plant(**parsed_val)
        _p.save()
    return redirect("/")
    
def add_compost(request):
    if request.method == "POST":
        time = str(request.POST.get("compost-date")) 
        c_date = datetime.strptime(time, '%d/%m/%Y')
        p_id = request.POST.get("p_id")
        c_type = request.POST.get("compost-type")
        c_total = request.POST.get("compost-total")
        c_unit = request.POST.get("compost-unit")
        parsed_val = parse_keys3(p_id, c_date, c_type, c_total, c_unit)
        _c = Compost(**parsed_val)
        _c.save()
    html = "/plant/view_compost/"+str(p_id)+"/"
    return redirect(html)
    
def del_vegetable(request):
    ids = json.loads(request.POST.get("delete-ids"))
    Vegetable.objects.filter(pk__in=ids).delete()
    return redirect("/vegetables/view/")
    
def del_compost(request):
    p_id = int(request.POST.get("p_id"))
    ids = json.loads(request.POST.get("delete-ids"))
    Compost.objects.filter(pk__in=ids).delete()
    html = "/plant/view_compost/"+str(p_id)+"/"
    return redirect(html)
    
def del_plant(request):
    id = int(request.POST.get("delete-id"))
    Plant.objects.filter(pk=id).delete()
    return redirect("/")
    
def edit_vegetable(request, id):
    _v = Vegetable.objects.get(pk=id)
    return render(request, "edit_vegetable.html", {
        "v": _v,
    })
def edit_compost(request):
    id = int(request.POST.get("c_id"))
    p_id = request.POST.get("p_id")
    time = str(request.POST.get("compost-date")) 
    c_date = datetime.strptime(time, '%d/%m/%Y')
    c_type = request.POST.get("compost-type")
    c_total = request.POST.get("compost-total")
    c_unit = request.POST.get("compost-unit")
    parsed_val = parse_keys3(p_id, c_date, c_type, c_total, c_unit)
    Compost.objects.filter(pk=id).update(**parsed_val)
    html = "/plant/view_compost/"+str(p_id)+"/"
    return redirect(html)
    
def keep_plant(request):
    if request.method == "POST":
        id = int(request.POST.get("p_id"))
        time = str(request.POST.get("keep-date")) 
        date = datetime.strptime(time, '%d/%m/%Y')
        total = request.POST.get("keep-total")
        unit = request.POST.get("keep-unit")
        parsed_val = parse_keys4(date, total, unit)
        Plant.objects.filter(pk=id).update(**parsed_val)
    return redirect("/")
    
def update_vegetable(request):
    id = int(request.POST.get("id"))
    parsed_val = parse_keys(Plant_keys, request.POST)
    Vegetable.objects.filter(pk=id).update(**parsed_val)
    return redirect("/vegetables/view/")
    
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
    result_x = refX.order_by_child('time').limit_to_last(288).get()
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
    result_a = refA.order_by_child('time').limit_to_last(288).get()
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
    result_b = refB.order_by_child('time').limit_to_last(288).get()
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
    result_c = refC.order_by_child('time').limit_to_last(288).get()
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
