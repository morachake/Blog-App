from django.urls import path
from .views import PostDetail,PostList

app_name = 'blog_api'

urlpatterns =[
    path('<int:pk>/', PostDetail.as_view(), name='detailcreated'),
    path('',PostList.as_view(), name='listcreated'),
]