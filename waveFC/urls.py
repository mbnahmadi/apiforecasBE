from django.urls import path
from waveFC.views import *

urlpatterns = [
    # path("", PointView, name="point"),
    # path("api/", serializer, name="api")
    # path("api/<n>", GetAl, name="api"),
    path('waveforecast/<str:name>/', GetAllData.as_view()),
    # path('api_csv/<str:name>/', GetAllCSVData.as_view()),
    # path('api/', GetListData.as_view()),
    path('list/', GetListData),
]