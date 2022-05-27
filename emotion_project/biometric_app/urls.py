from django.contrib import admin
from django.urls import path
from django.urls import include, path
from biometric_app import views

urlpatterns = [
    path('', views.index,name='index'),
    path('video_feed', views.video_feed,name='video_feed'),
    path('refresh', views.refresh, name='refresh'),
    path('search_result', views.search_result, name='search_result'),
    path('capture_video', views.capture_video,name='capture_video'),
    path('unregisterd', views.unregisterd, name='unregisterd'),
    path('training', views.training, name='training'),
    path('registerd_people', views.registerd_people, name='registerd_people'),
    path('unknown-search', views.unknown_search, name='unknown_search'),
    path('checking_individual', views.checking_individual, name='checking_individual'),
    path('uncheck', views.uncheck, name='uncheck'),






]