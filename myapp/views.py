from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

# Create your views here.
@api_view(["POST","GET"])
def index(request):
    if request.method == "POST":
        data=request.data.get("data")
        if data is list:
            pass
        else:
            return Response(alldata(data))
        return Response({"msg":data})
    else:
        return Response({"msg":"success","info":"The API is working, please look into documentation to get desired response."})
    
def alldata(data):
    json_data = open('E:/Codes/django/projects/localbody/static/local_level.json')
    main_data = json.load(json_data)
    json_data.close()
    if data=="Districts":
        districts=[]
        for province in main_data:
            for dists in main_data[province]:
                districts.append(list(dists.keys())[0])
        return {"msg":"success","info":"Districs list is sent..","data":districts} 
    elif data == "Provinces":
        return {"msg":"success","info":"Districs list is sent..","data":list(main_data.keys())}