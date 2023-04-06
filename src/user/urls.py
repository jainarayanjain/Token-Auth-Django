from django.urls import include, path
from user.views import GetRequest,CustomAuthToken
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [

    path('crudoperations/', GetRequest.as_view({'get': 'list', 'post': 'create'}), name="list"),
    path('crudoperations/<int:pk>/',
         GetRequest.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('gettoken/', obtain_auth_token), # normal token
    path('login/',CustomAuthToken.as_view()) # customized data with token
]
