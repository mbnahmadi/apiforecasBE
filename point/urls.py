from django.urls import path
from point.views import *

urlpatterns = [
    # path("", PointView, name="point"),
    # path("api/", serializer, name="api")
    # path("api/<n>", GetAl, name="api"),
    path('api/<str:name>/', GetAllData.as_view()),
    # path('api_csv/<str:name>/', GetAllCSVData.as_view()),
    # path('api/', GetListData.as_view()),
    path('api/', GetListData),
    path('name/',get_name),
]

# for item in items:
#     new_url = f"api/{item}/"
#     urlpatterns.append(path(f"api/{item}/", GetAlData.as_view(item='<f"api/{item}/">')))
    
# path(f"api/{item}/", GetAllData.as_view(), name="api")
