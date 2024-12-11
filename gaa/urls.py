# from django.urls import path
#
#
# from . import views
# #
# urlpatterns = [
#     path('hello/',views.say_helo)
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('', views.say_hello),


]