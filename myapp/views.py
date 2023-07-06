from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from datas import all_districts, all_localbody, all_provinces
# Create your views here.
@api_view(["POST","GET"])
def index(request):
    if request.method == "POST":
        data=request.data.get("data")
        if type(data) is dict:
            if list(data.keys())==["District"]:
                if data["District"] in all_districts:
                    return Response(district(data["District"]))
                else:
                    return Response({'msg':'error','info':"Entered district doesn't exist"})
        else:
            return Response(alldata(data))
        # return Response({"msg":data})
    else:
        return Response({"msg":"success","info":"The API is working, please look into documentation to get desired response."})
    
def alldata(data):
    if data=="Districts":
        return {"msg":"success","info":"Districs list is sent..","data":all_districts} 
    elif data == "Provinces":
        return {"msg":"success","info":"Districs list is sent..","data":all_provinces}
    elif data == "Local_bodies":
        return {"msg":"success","info":"Local Bodies list is sent..","data":all_localbody} 
    else:
        return({"msg":"error","info":"POST is invalid, please refer to documentation for info.."})

def district(district):
    json_data = open('E:/Codes/django/projects/localbody/static/local_level.json')
    main_data = json.load(json_data)
    json_data.close()
    final=[]
    for province in main_data:
        for dists in main_data[province]:
            if district==list(dists.keys())[0]:
                final.append(dists[district])
    return ({"msg":"success","info":f"Local_bodies in {district} district is sent.","data":final[0]})