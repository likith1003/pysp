from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('placement',views.placement,name='placement'),
    path('pythond',views.pythond,name='pythond'),
    path('pythonmt',views.pythonmt,name='pythonmt'),
    path('pythonat',views.pythonat,name='pythonat'),
    path('sql',views.sql,name='sql'),
    path('web',views.web,name='web'),
    path('verbal',views.verbal,name='verbal'), 
    path('apti',views.apti,name='apti'),
    path('contact',views.contact,name='contact'),
    path('fresher',views.fresher,name='fresher'),
    path('exp',views.exp,name='exp'),    
]