from urllib import response
from django.shortcuts import render, redirect
import numpy as np
import pandas as pd
from .point_name import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DataSerializer, NameSerializer
import os
from django.http import Http404
from django.http import HttpResponse

items = os.listdir("./None")



def get_name(self):
    for name in items:
        print(name)
    #return HttpResponse(name)

def make_dict(data):
    for i in range(len(data)):
        keys    = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7']
        values  = data[i]
        base_dict = { key : value for key, value in zip(keys, values) }
        data_dic.append(base_dict)
        
        
# def make_dict_csv(mydata):
#     for i in range(len(mydata)):
#         keys_csv    = ['a1', 'a2', 'a3', 'a4', 'a5']
#         values_csv  = mydata[i]
#         base_dict_csv = { key : value for key, value in zip(keys_csv, values_csv) }
#         data_dic_csv.append(base_dict_csv)        





# class GetAllCSVData(APIView):
#     def get_object(self, name):
#         try:
#             return name in items
#         except items.DoesNotExist:
#             raise Http404            
    
#     def get_excel_object(self , request , name , format=None):
#         global data_dic_csv
#         mydata= np.genfromtxt((f"None\{name}.csv"),dtype=None, delimiter="")
#         # data = pd.read_csv((f"None\{name}.csv"), header=1)
#         data_dic_csv = []
#         make_dict_csv(mydata)
#         query = data_dic_csv
#         myserializer = CSVDataSerializer(query, many=True)
#         return Response(myserializer.data, status=status.HTTP_200_OK)



from django.core import serializers
class GetAllData(APIView):
    def get_object(self, name):
        try:
            return name in items
        except items.DoesNotExist:
            raise Http404
    def get(self, request, name, format=None):
        global data_dic
        data= np.genfromtxt((f"None\{name}.mean"),dtype=None, delimiter="")
        data_dic = []
        make_dict(data)
        query = data_dic
        serializer = DataSerializer(query, many=True).data
        
        name_dic = { 'name' : name}
        name_ser = NameSerializer(name_dic).data
        serializer.append(name_ser)
        return Response(serializer, status=status.HTTP_200_OK)
    
    




    
    
    
    
# class GetAllData(APIView):
#     def get_object(self, pk):
#         try:
#             return items[pk]
#         except items.DoesNotExist:
#             raise Http404
#     def get(self, request, pk, format=None):
#         global data_dic
#         item = self.get_object(pk)
#         data= np.genfromtxt((f"None\{item}"),dtype=None, delimiter="")
#         data_dic = []
#         base_dict = {}
#         make_dict(data)
#         query = data_dic
#         serializer = DataSerializer(query, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
# class GetListData(APIView):
#     def get_object(self):
#         try:
#             return items
#         except items.DoesNotExist:
#             raise Http404
#     def get(self, request, format=None):
#         items = self.get_object()
#         print("/////////////////////////", items)
#         keys=[]
#         values=[]
#         for i, item in enumerate(items): 
#             keys.append(i)
#             values.append(item)
#         data = { key : value for key, value in zip(keys, values) }
#         print("/////////////////////////",data)
#         query = data
#         serializer = DataSerializer(query, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(status=status.HTTP_200_OK)
    
    
from rest_framework.decorators import api_view
@api_view()
def GetListData(request):
    # keys=[]
    # values=[]
    # for i, item in enumerate(items): 
    #     keys.append(i)
    #     values.append(item)
    # data = { key : value for key, value in zip(keys, values) }
    # print("/////////////////////////",data)
    return Response(items)


    
# for item in items:
#     global data_dic
#     print (item)
#     data= np.genfromtxt((f"None\{item}"),dtype=None, delimiter="")
#     data_dic = []
#     base_dict = {}
#     dict(data)
#     print (data)    
#     class searchpoint(APIView):
#         def get(self,request):
#             search = request.GET["point_name"]
#             query = data_dic
#             serializer = DataSerializer(query, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
    
# def GetAl(request, n):
#     return render(request, 'point/point.html', {'n' : n})

# class GetAlData(APIView):
#     global data_dic
#     data= np.genfromtxt((f"None\{items[1]}"),dtype=None, delimiter="")
#     data_dic = []
#     base_dict = {}
#     dict(data)
#     print (data)
#     def get(self, request):
#         query = data_dic
#         serializer = DataSerializer(query, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    

# def PointView (request):
#     # context = {
#     #     "data_dic" : data_dic,
#     # }
#     return render(request, "point/point.html")





