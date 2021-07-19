
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'index'),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("investor",views.investor,name="investor"),
    path("promoter",views.promoter,name="promoter"),
    path("bussquery",views.bussquery,name="bussquery"),
    path("like",views.like,name="like"),
    path("postbus",views.postbus,name="postbus"),
    path("search",views.search,name="search"),
    path("startup",views.startup,name="startup"),
    path("poststartup",views.poststartup,name="poststartup"),
    path("myads",views.myads,name="myads"),
    
]
