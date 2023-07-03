from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

# Create your views here.
@api_view(["POST","GET"])
def index(request):
    json_data = open('E:/Codes/django/projects/localbody/static/js/local_level.json')
    data1 = json.load(json_data)
    json_data.close()
    return Response({"OK":data1})