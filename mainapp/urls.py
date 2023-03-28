from django.urls import path
from .import views

urlpatterns=[
    path("", views.HomePageView.as_view(),name="home"),
    path("request_data/",views.fetchdata, name="featchdata"),
    path("dashboard/",views.dashboard, name="dashboard"),
    path("dashboard_fetchdata/",views.dashboard_fetchdata, name="dashboard_fetchdata")
    
]