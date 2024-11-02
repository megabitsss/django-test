from django.urls import path
from mypage import views

urlpatterns = [
    path('',views.index),
    path('creative.html',views.creative),
    path('index.html',views.index),
    path('checkscreative.html',views.room)
]