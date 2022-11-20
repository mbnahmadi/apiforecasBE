from django.shortcuts import render
import numpy as np
import pandas as pd
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CSVDataSerializer
import os
from django.http import Http404

# Create your views here.

items = os.listdir("./None")

def make_dict_csv(data):
    for i in range(len(data)):
        keys    = ['a1', 'a2', 'a3', 'a4', 'a5']
        values  = data.loc[i]
        base_dict_csv = { key : value for key, value in zip(keys, values) }
        data_dic_csv.append(base_dict_csv)        


class GetAllData(APIView):
    def get_object(self, name):
        try:
            return name in items
        except items.DoesNotExist:
            raise Http404
    def get(self, request, name, format=None):
        global data_dic_csv
        # data= np.genfromtxt((f"None\{name}.mean"),dtype=None, delimiter="")
        df = pd.read_csv((f"None\{name}.csv"), header=3)
        data = df.drop(df.columns[[1,2,3,4,6,9,10,11,12,13,14,15]],axis=1)
        data_dic_csv = []
        make_dict_csv(data)
        query = data_dic_csv
        serializer = CSVDataSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    





from rest_framework.decorators import api_view
@api_view()
def GetListData(request):
    return Response(items)



