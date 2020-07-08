from django.urls import path,include
from complain import views

urlpatterns = [
    path('', views.add_complain, name="add_complain" ),
    path("done/", views.done, name="done"),
    path("msg/", views.member_msg, name="msg_from_member")
]
